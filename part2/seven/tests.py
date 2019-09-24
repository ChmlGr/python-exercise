from django.test import TestCase
from . import utils


class SevenTestCase(TestCase):
    def test_find_pairs(self):
        values = [1, 2, 5, 7, 8, 0, 4, 3]
        self.assertEqual(utils.find_pairs(values, 7), [(5, 2), (0, 7), (3, 4)])
