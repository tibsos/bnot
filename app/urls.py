from django.urls import path

from .views import *

app_name = 'app'

urlpatterns = [

    path('home/', home, name = 'home'),

]

htmx_urlpatterns = [

    path('create-note/', create_note, name = 'create-note'),
    path('create-folder/', create_folder, name = 'create-folder'),

    path('add-image-to-new-note/', add_image_to_new_note, name = 'add-image-to-new-note'),

]

urlpatterns += htmx_urlpatterns