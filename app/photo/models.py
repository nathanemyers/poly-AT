from __future__ import unicode_literals

from django.db import models

from PIL import Image
import numpy as np

from app.rgb.models import RGB
from .blockwise_view import blockwise_view


def calculate_color_sum(arr):
    mean = arr.mean(0).mean(0)

    return mean


class Photo(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(height_field="height", width_field="width", upload_to="static/tmp")
    height = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    rgb = models.ForeignKey(RGB, blank=True, null=True)

    def to_array(self):
        if (self.image is None):
            return []

        image_file = self.image.file
        pillow = Image.open(image_file.name)
        arr = np.asarray(pillow)

        return arr

    def pixelize(self, width, height):
        if (self.image is None):
            return []

        arr = self.to_array()
        blocked_array = blockwise_view(
            arr,
            blockshape=(width, height, 3),
            require_aligned_blocks=False
        )
        x, y, z, a, b, c, = blocked_array.shape
        summed_color = np.zeros((x, y, 3), dtype=float, order='C')

        for index in np.ndindex(x, y):
            block = blocked_array[index][0]
            color_sum = calculate_color_sum(block)
            summed_color[index] = color_sum

        return summed_color

    def save(self, *args, **kwargs):
        color_sum = calculate_color_sum(self.to_array())
        self.rgb = RGB(
            r=color_sum[0],
            g=color_sum[1],
            b=color_sum[2],
        ).save()
        super(Photo, self).save(*args, **kwargs)
