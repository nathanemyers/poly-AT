import os
from django.test import TestCase
from django.core.files import File

from app.photo.models import Photo, calculate_color_sum


class PhotoTests(TestCase):
    def setUp(self):
        test_image_path = 'static/test/woods.jpg'
        self.photo = Photo()
        self.photo.image.save(
            os.path.basename(test_image_path),
            File(open(test_image_path))
        )
        self.photo.save()

    def test_height(self):
        self.assertEqual(self.photo.height, 2448)

    def test_width(self):
        self.assertEqual(self.photo.width, 3264)

    def test_color_sum(self):
        result = calculate_color_sum(self.photo.to_array())
        self.assertEqual(result.r, 58.981953054914875)

    def test_pixelize(self):
        result = self.photo.pixelize(10, 10)

