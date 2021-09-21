from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        # if request.POST.get('method') == 'DELETE':
        # if request.POST.get('method') == 'UPDATE':
        # if request.POST.get('method') == 'POST':
        note = Note()
        note.title = request.POST.get('titulo')
        note.content = request.POST.get('detalhes')
        note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/notes.html', {'notes': all_notes})

def updateViews(request, pk):
    Note.objects.filter(pk=pk).update(title=request.POST.get('title'), content=request.POST.get('content'))
    return redirect('index')


def deleteView(request, pk):
    note_delete = Note.objects.get(pk=pk)
    note_delete.delete()
    return redirect('index')