from django.test import TestCase
from django.core.files import File

from app.photo.models import Photo, add_colors
from app.rgb.models import RGB


class PhotoTests(TestCase):
    def setUp(self):
        test_image = File(open('static/test/woods.jpg'))
        self.photo = Photo()
        self.photo.image.save('test_image', test_image)

    def test_height(self):
        self.assertEqual(self.photo.height, 2448)

    def test_width(self):
        self.assertEqual(self.photo.width, 3264)

    def test_color_sumnation(self):
        self.assertEqual(self.photo.sum_color, RGB())

    def test_add_colors(self):


