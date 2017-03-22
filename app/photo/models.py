from __future__ import unicode_literals

from django.db import models
from PIL import Image
import numpy as np

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

        image_file = self.image.file
        pillow = Image.open(image_file.name)
        arr = np.asarray(pillow)
        mean = arr.mean(0).mean(0)

        return RGB(r=mean[0], g=mean[1], b=mean[2])


