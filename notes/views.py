from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        note = Note()
        note.title = request.POST.get('titulo')
        note.content = request.POST.get('detalhes')
        note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/notes.html', {'notes': all_notes})