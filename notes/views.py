from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        if request.POST.get('method') == 'DELETE':
            note_delete = Note.objects.get(pk=request.POST.get('id'))
            note_delete.delete()
        if request.POST.get('method') == 'UPDATE':
            Note.objects.filter(id=request.POST.get('id')).update(title=request.POST.get('title'), content=request.POST.get('content'))
        if request.POST.get('method') == 'POST':
            note = Note()
            note.title = request.POST.get('titulo')
            note.content = request.POST.get('detalhes')
            note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/notes.html', {'notes': all_notes})