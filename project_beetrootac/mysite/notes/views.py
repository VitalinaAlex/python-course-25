from django.shortcuts import render, redirect, get_object_or_404
from .models import Note, Category
from .forms import NoteForm
from django.utils.timezone import now

def index(request):
    notes = Note.objects.all()

    category_id = request.GET.get('category')
    search = request.GET.get('search')
    reminder = request.GET.get('reminder')

    if category_id:
        notes = notes.filter(category_id=category_id)

    if search:
        notes = notes.filter(title__icontains=search)

    if reminder == 'future':
        notes = notes.filter(reminder__gt=now())

    categories = Category.objects.all()

    return render(request, 'notes/index.html', {
        'notes': notes,
        'categories': categories
    })


def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NoteForm()

    return render(request, 'notes/note_form.html', {'form': form})

def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_detail', pk=pk)
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/note_detail.html', {
        'note': note,
        'form': form
    })

def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == 'POST':
        note.delete()
        return redirect('index')

    return render(request, 'notes/note_delete.html', {'note': note})
# Create your views here.