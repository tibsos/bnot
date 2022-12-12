from django.shortcuts import render

def landing(request):

    c = {}

    if request.user.is_authenticated:

        c['u'] = True

    else:

        c['u'] = False

    return render(request, 'landing.html', c)