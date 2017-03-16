from __future__ import unicode_literals

from django.db import models

from app.rgb.models import RGB


class Photo(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(height_field="height", width_field="width", upload_to="static/tmp")
    height = models.IntegerField()
    width = models.IntegerField()
    rgb = models.ForeignKey(RGB, blank=True, null=True)

    def caluculate_color_sum(self):
        if (self.image is None):
            return RGB()

        pixels = list(self.image.getdata())

