import unittest
from . import commons


class PalindromeTest(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertEqual(commons.is_palindrome('tacocat'), True)
        self.assertEqual(commons.is_palindrome('taco-cat'), True)

    def test_is_palindrome_phrase(self):
        self.assertEqual(commons.is_palindrome('Madam, I\'m Adam'), True)

    def test_is_not_palindrome(self):
        self.assertEqual(commons.is_palindrome('catdog'), False)
