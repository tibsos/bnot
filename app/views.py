from django.shortcuts import render

from django.contrib.auth.decorators import login_required as lr

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

    if folders:

        folders = folders.split(' ')

        for folder in folders:

            note.folders.add(Folder.objects.get(uid = folder))

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