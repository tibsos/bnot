from django.urls import path

from .views import *

urlpatterns = [

    path('login/', log_in, name = 'login'),
    path('register/', register, name = 'register'),

]