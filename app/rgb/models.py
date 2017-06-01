from __future__ import unicode_literals

from django.db import models


def sum_colors(color_array):
    length = len(color_array)
    r = reduce(lambda a, b: a.r + b.r, color_array)
    g = reduce(lambda a, b: a.g + b.g, color_array)
    b = reduce(lambda a, b: a.b + b.b, color_array)
    return RGB(
        r=r / length,
        g=g / length,
        b=b / length
    )


class RGB(models.Model):
    r = models.IntegerField(default=0)
    g = models.IntegerField(default=0)
    b = models.IntegerField(default=0)

    def __str__(self):
        return "({}, {}, {})".format(self.r, self.g, self.b)

    @classmethod
    def create(cls, rgb_tuple):
        RGB = cls(
            r=rgb_tuple[0],
            g=rgb_tuple[1],
            b=rgb_tuple[2],
        )
        RGB.save()
        return RGB
