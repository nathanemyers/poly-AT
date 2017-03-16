from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from app.photo.models import Photo
from app.rgb.models import RGB


class PhotoTests(TestCase):
    def setUp(self):
        self.photo = Photo()
        self.photo.image = SimpleUploadedFile(
            name='woods.jpg',
            content=open('static/test/', 'rb').read(),
            content_type='image/jpeg'
        )

    def test_height(self):
        self.assertEqual(self.photo.height, 0)

    def test_width(self):
        self.assertEqual(self.photo.width, 0)

    def test_color_sumnation(self):
        self.assertEqual(self.photo.sum_color, RGB())




