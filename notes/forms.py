from django import forms
from .models import Category,Note

class NoteForm(forms.ModelForm):
    model = Note
    fields = ['title', 'content', 'category', 'tags', 'is_pinned']
    # TODO Maybe if i change class attrs with Bootstrap classes it looks for good
    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title...'}),
        'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Text of the note...'}),
        'category': forms.Select(attrs={'class': 'form-select'}),
        'tags': forms.SelectMultiple(attrs={'class': 'form-select'}),
        'is_pinned': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(NoteForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['category'].queryset = Category.objects.filter(owner=user)