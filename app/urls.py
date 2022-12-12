from django.urls import path

from .views import *

app_name = 'app'

urlpatterns = [

    path('home/', home, name = 'home'),

]

htmx_urlpatterns = [

    path('create-note/', create_note, name = 'create-note'),
    path('create-folder/', create_folder, name = 'create-folder'),

    path('folder-notes/<uuid:uid>/', folder_notes, name = 'folder-notes'),

    path('search-notes/', search_notes, name = 'search-notes'),
    path('get-note/<uuid:uid>/', get_note, name = 'get-note'),

    path('archive-note/<uuid:uid>/', archive_note, name = 'archive-note'),

    path('add-image-to-new-note/', add_image_to_new_note, name = 'add-image-to-new-note'),

]

urlpatterns += htmx_urlpatterns