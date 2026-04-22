# test_string_processor_p49.py
import unittest
from string_processsor import StringProcessor

class TestStringProcessor(unittest.TestCase):

    def test_reverse(self):
        calc = StringProcessor()
        self.assertEqual(calc.reverse("abc"), "cba")

    def test_count_vowels(self):
        calc = StringProcessor()
        self.assertEqual(calc.count_vowels("apple"), 2)

    def test_is_palindrome(self):
        calc = StringProcessor()
        self.assertTrue(calc.is_palindrome("ab c ba"))
        self.assertFalse(calc.is_palindrome("ABnCA"))

if __name__ == '__main__':
    unittest.main()