from django.shortcuts import render

from django.contrib.auth.decorators import login_required as lr

from django.db.models import Q
from .models import *

@lr
def home(request):

    user = request.user

    notes = Note.objects.filter(user = user).filter(deleted = False)

    pinned_notes = notes.filter(pinned = True)
    notes = notes.filter(pinned = False)

    c = {}

    c['folders'] = Folder.objects.filter(user = user)

    c['pinned_notes'] = pinned_notes
    c['notes'] = notes

    return render(request, 'home.html', c)


# htmx

@lr
def create_note(request):

    user = request.user

    pinned = request.POST.get('pinned')

    if pinned == 'on':
        pinned = True
    else:
        pinned = False

    loved = request.POST.get('loved')

    if loved == 'on':
        loved = True
    else:
        loved = False


    note_uid = request.POST.get('note-uid')

    if note_uid:

        note = Note.objects.get(uid = note_uid)

        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.pinned = pinned
        note.loved = loved

    else:

        note = Note.objects.create(

            user = user,

            title = request.POST.get('title'),
            content = request.POST.get('content'),

            pinned = pinned,
            loved = loved,

        )
    
    folders = request.POST.get('folders')


    c = {}

    notes = Note.objects.filter(user = user).filter(deleted = False)

    pinned_notes = notes.filter(pinned = True)
    notes = notes.filter(pinned = False)

    c = {}


    c['pinned_notes'] = pinned_notes
    c['notes'] = notes

    return render(request, 'components/notes.html', c)

@lr
def create_folder(request):

    Folder.objects.create(

        user = request.user,

        title = request.POST.get('title')

    )

    return render(request, 'components/folders.html', {'folders': Folder.objects.filter(user = request.user)})

@lr
def folder_notes(request, uid):

    folder = Folder.objects.get(uid = uid)

    notes = Note.objects.filter(folders__in = [folder])

    c = {}

    c['notes'] = notes

    return render(request, 'components/notes.html', c)

@lr
def get_note(request, uid):
    return render(request, 'components/note.html', {'note': Note.objects.get(uid = uid)})

@lr
def search_notes(request):

    q = request.POST.get('q')

    if q == '':

        notes = None

    else:

        notes1 = list(Note.objects.filter(title__contains = q))
        notes2 = list(Note.objects.filter(content__contains = q))
        notes = set(notes1 + notes2)

    return render(request, 'components/found-notes.html', {'r': notes})

@lr
def add_image_to_new_note(request):

    note_uid = request.POST.get("note-uid")

    if note_uid:

        note = Note.objects.get(uid = note_uid)

    else:

        note = Note.objects.create(
            user = request.user,
        )    

    image = Image.objects.create(

        user = request.user,

        note = note,

        file = request.FILES.get('image'),

    )

    note.images.add(image)

    return render(request, 'components/new-note-images.html', {'note': note})

@lr
def archive_note(request, uid):

    note = Note.objects.get(uid = uid)
    note.archived = not note.archived
    note.save()

    # return notes

    c = {}

    return render(request, 'components/notes.html', c)


def delete_notes(notes):

    for note in notes:

        pass

        # if difference between now & deleted at > 30 days
            # delete note from db 