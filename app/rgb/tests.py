from django.test import TestCase

from app.rgb.models import RGB


class RGBTests(TestCase):
    def setUp(self):
        pass

    def test_add_colors(self):
        pass

    def test_create(self):
        result = RGB.create((100, 200, 50))
        self.assertEqual(result.r, 100)
        self.assertEqual(result.g, 200)
        self.assertEqual(result.b, 50)

