from django.shortcuts import render

from app.photo.models import Photo


def index(request):
    test = Photo.objects.first()
    context = {
        "pixels": test.pixelize()
    }

    return render(request, 'index.html', context=context)
