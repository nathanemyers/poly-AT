from __future__ import unicode_literals

from django.db import models
from PIL import Image

from app.rgb.models import RGB, sum_colors


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
        # import pdb;pdb.set_trace()
        pillow = Image.open(image_file.name)

        pixels = list(pillow.getdata())
        rgb_pixels = map(lambda x: RGB.create(x), pixels)
        return sum_colors(rgb_pixels)

