from __future__ import unicode_literals

from django.db import models


def add_colors(color1, color2):
    pass


class RGB(models.Model):
    r = models.IntegerField(default=0)
    g = models.IntegerField(default=0)
    b = models.IntegerField(default=0)

    def __str__(self):
        return "({}, {}, {})".format(self.r, self.g, self.b)

    @classmethod
    def create(cls, rgb_tuple):
        return cls(
            r=rgb_tuple[0],
            g=rgb_tuple[1],
            b=rgb_tuple[2],
        )
