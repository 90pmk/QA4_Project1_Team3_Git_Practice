import unittest

class TestStringUtils(unittest.TestCase):

    def test_upper(self):
        result = "hello".upper()
        self.assertEqual(result, "HELLO")

    def test_lower(self):
        result = "WORLD".lower()
        self.assertEqual(result, "world")

    def test_strip(self):
        result = "  hello  ".strip()
        self.assertEqual(result, "hello")

if __name__ == '__main__':
    unittest.main()