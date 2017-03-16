from django.test import TestCase

from app.photo.models import Photo
from app.rgb.models import RGB


class PhotoTests(TestCase):
    def set_up(self):
        self.photo = Photo()

    def test_height(self):
        self.assertEqual(self.height, 0)

    def test_width(self):
        self.assertEqual(self.width, 0)

    def test_color_sumnation(self):
        self.assertEqual(self.sum_color, RGB())
