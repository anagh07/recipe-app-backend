"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc

class SampleTest(SimpleTestCase):

    def test_add(self):
        result = calc.add(1, 1)
        self.assertEqual(result, 2)

    def test_subtract(self):
        result = calc.subtract(7, 2)
        self.assertEqual(result, 5)
