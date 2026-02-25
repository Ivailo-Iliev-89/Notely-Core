from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from rest_framework import viewsets, permissions
from .serializers import NoteSerializer
from django import forms
from .models import Tag, Note, Category
from django.db.models import Q


class OwnerQuerySetMixin(LoginRequiredMixin):
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)


class NoteListView(OwnerQuerySetMixin, ListView):
    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'
    paginate_by = 5 

    def get_queryset(self):
        queryset = super().get_queryset().select_related('category')
        q = self.request.GET.get('q')
        cat_id = self.request.GET.get('category')
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) |
                Q(content__icontains=q) |
                Q(tags__name__icontains=q)
            ).distinct()

        if cat_id:
            queryset = queryset.filter(category_id=cat_id)
            
        return queryset


class NoteDetailView(OwnerQuerySetMixin, DetailView):
    model = Note
    template_name = 'notes/note_detail.html'
    context_object_name = 'note'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'content', 'category', 'tags']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note-list')

    def get_form(self, form_class=None):
        """"Change tags vision to checkboxes"""

        form = super().get_form(form_class)
        form.fields['tags'].widget = forms.CheckboxSelectMultiple()
        form.fields['tags'].queryset = Tag.objects.all()

        form.fields['category'].queryset = Category.objects.filter(owner=self.request.user)
        form.fields['category'].widget.attrs.update({'class': 'form-select'})
        return form

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class NoteUpdateView(OwnerQuerySetMixin, UpdateView):
    model = Note
    fields = ['title', 'content', 'category', 'tags']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note-list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['tags'].widget = forms.CheckboxSelectMultiple()
        form.fields['tags'].queryset = Tag.objects.all()
        
        form.fields['category'].queryset = Category.objects.filter(owner=self.request.user)
        form.fields['category'].widget.attrs.update({'class': 'form-select'})
        return form


class NoteDeleteView(OwnerQuerySetMixin, DeleteView):
    model = Note
    template_name = 'notes/note_delete.html'
    success_url = reverse_lazy('note-list')


class IsOwnerReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Note.objects.filter(owner=user).order_by('-created_at')
        return Note.objects.none()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
