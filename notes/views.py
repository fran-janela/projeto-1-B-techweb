from django.db.models.query import EmptyQuerySet, QuerySet
from django.shortcuts import render, redirect
from .models import Note, Tag


def indexNote(request):
    if request.method == 'POST':
        note = Note()
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        
        tag_name = request.POST.get('tag')
        if tag_name != '':
            tag, create = Tag.objects.get_or_create(name=tag_name)
            if create:
                tag.color = request.POST.get('color')
                tag.save()
            
            note.tag = tag
        note.save()
        return redirect('indexNote')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/notes.html', {'notes': all_notes})

def updateNoteViews(request, pk):
    note = Note.objects.get(pk=pk)
    previous_tag = note.tag

    tag_name = request.POST.get('tag')
    if tag_name != '':
        tag, create = Tag.objects.get_or_create(name=tag_name)
        if create:
            tag.color = request.POST.get('color')
            tag.save()
        elif tag.color != request.POST.get('color'):
            tag.color = request.POST.get('color')
            tag.save()
        Note.objects.filter(pk=pk).update(title=request.POST.get('title'), content=request.POST.get('content'), tag=tag)
    else:
        Note.objects.filter(pk=pk).update(title=request.POST.get('title'), content=request.POST.get('content'))

    if previous_tag:
        existing_notes = Note.objects.filter(tag=previous_tag)
        if not existing_notes:
            previous_tag.delete()
    return redirect('indexNote')


def deleteNoteView(request, pk):
    note_delete = Note.objects.get(pk=pk)
    tag = note_delete.tag
    note_delete.delete()
    if tag:
        existing_notes = Note.objects.filter(tag=tag)
        if not existing_notes:
            tag.delete()
    return redirect('indexNote')


def indexTag(request):
    all_tags = Tag.objects.all()
    return render(request, 'tags/tags.html', {'tags': all_tags})
    

def detailTag(request, pk):
    tag = Tag.objects.get(pk=pk)
    selected_notes = Note.objects.filter(tag=tag)
    return render(request, 'tags/selected.html', {'notes': selected_notes})