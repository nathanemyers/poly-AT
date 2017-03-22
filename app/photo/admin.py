from django.contrib import admin
from app.photo.models import Photo


class PhotoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Photo, PhotoAdmin)
