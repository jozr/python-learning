import unittest

import main
from main import reverse_string


class ReverseStringTests(unittest.TestCase):
    def test_cellar_door(self):
        result = reverse_string("cellar door")
        self.assertEqual(result, "rood rallec")

    def test_racecar(self):
        result = reverse_string("racecar")
        self.assertEqual(result, "racecar")
