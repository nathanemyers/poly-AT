from django.test import TestCase

from app.rgb.models import RGB, add_colors


class RGBTests(TestCase):
    def setUp(self):
        pass

    def test_add_colors(self):
        c1 = RGB.create((100, 120, 50))
        c2 = RGB.create((20, 255, 30))
        result = add_colors(c1, c2)
        self.assertEqual(result.r, 60)
        self.assertEqual(result.g, 187)
        self.assertEqual(result.b, 40)

    def test_create(self):
        result = RGB.create((100, 200, 50))
        self.assertEqual(result.r, 100)
        self.assertEqual(result.g, 200)
        self.assertEqual(result.b, 50)

