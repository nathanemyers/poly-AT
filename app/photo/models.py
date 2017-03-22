from __future__ import unicode_literals

from django.db import models
from PIL import Image
import numpy as np

from app.rgb.models import RGB
from .blockwise_view import blockwise_view


def calculate_color_sum(arr):
    mean = arr.mean(0).mean(0)

    return RGB(r=mean[0], g=mean[1], b=mean[2])


class Photo(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(height_field="height", width_field="width", upload_to="static/tmp")
    height = models.IntegerField()
    width = models.IntegerField()
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
        blocked_array = blockwise_view(arr, blockshape=(30, 30, 3), require_aligned_blocks=False)
        import pdb;pdb.set_trace()
        map(lambda x: calculate_color_sum(x), blocked_array)
        return arr

