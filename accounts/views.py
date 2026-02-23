from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from notes.models import Note


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
    notes = Note.objects.filter(owner=request.user).order_by('-is_pinned', '-created_at')
    return render(request, 'accounts/dashboard.html', {'notes': notes})

@login_required
def toggle_pin(request, note_id):
    '''Take the note , if only is the current user and pinned'''
    note = get_object_or_404(Note,id=note_id,owner=request.user)
    note.is_pinned = not note.is_pinned
    note.save()
    return redirect('dashboard')
