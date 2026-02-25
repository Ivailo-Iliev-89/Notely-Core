from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from notes.models import Note,Category


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def dashboard(request):
    query = request.GET.get('q')
    category_id = request.GET.get('category')
    notes = Note.objects.filter(owner=request.user).select_related('category')
    
    # Filter by searching
    if query:
        notes= notes.filter(title__icontains=query)
    # Filter by category
    if category_id:
        notes = notes.filter(category_id=category_id)

    notes = notes.order_by('-is_pinned', '-created_at')
    categories = Category.objects.filter(owner=request.user)
    
    return render(request,'notes/note_list.html',{
                  'notes': notes,
                  'categories': categories
                  })

@login_required
def toggle_pin(request, note_id):
    '''Take the note , if only is the current user and pinned'''
    note = get_object_or_404(Note,id=note_id,owner=request.user)
    note.is_pinned = not note.is_pinned
    note.save()
    return redirect('note-list')
