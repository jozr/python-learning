import unittest

import main
from main import fizzbuzz


class FizzBuzzTests(unittest.TestCase):
    def test_fizz(self):
        result = fizzbuzz([3])
        self.assertEqual(result, 'Fizz')

    def test_buzz(self):
        result = fizzbuzz([5])
        self.assertEqual(result, 'Buzz')

    def test_fizzbuzz(self):
        result = fizzbuzz([15])
        self.assertEqual(result, 'FizzBuzz')

    def test_integer(self):
        result = fizzbuzz([4])
        self.assertEqual(result, "4")

    def test_multiple_possibilities(self):
        result = fizzbuzz([5, 0, 1, 19, 30, 130])
        self.assertEqual(result, "Buzz FizzBuzz 1 19 FizzBuzz Buzz")
