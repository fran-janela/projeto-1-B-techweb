from django.shortcuts import render, redirect
from .models import Note, Tag


def indexNote(request):
    if request.method == 'POST':
        note = Note()
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        
        tag_name = request.POST.get('tag')
        tag, create = Tag.objects.get_or_create(name=tag_name)
        if create:
            tag.save()
        
        note.tag = tag
        note.save()
        return redirect('indexNote')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/notes.html', {'notes': all_notes})

def updateNoteViews(request, pk):
    tag_name = request.POST.get('tag')
    tag, create = Tag.objects.get_or_create(name=tag_name)
    if create:
        tag.save()
    Note.objects.filter(pk=pk).update(title=request.POST.get('title'), content=request.POST.get('content'), tag=tag)
    return redirect('indexNote')


def deleteNoteView(request, pk):
    note_delete = Note.objects.get(pk=pk)
    note_delete.delete()
    return redirect('indexNote')


def indexTag(request):
    all_tags = Tag.objects.all()
    print('oie')
    return render(request, 'tags/tags.html', {'tags': all_tags})
    

def detailTag(request, pk):
    tag = Tag.objects.get(pk=pk)
    selected_notes = Note.objects.filter(tag=tag)
    return render(request, 'notes/notes.html', {'notes': selected_notes})