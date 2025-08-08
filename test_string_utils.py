import unittest

from string_utils import reverse_string, capitalize_string, is_capitalized

class TestStringUtils(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string('grape'),'eparg' )

    def test_capitalize_string(self):
        self.assertEqual(capitalize_string('grape'), 'Grape')

    def test_is_capitalized(self):
        self.assertTrue(is_capitalized('grape'))

if __name__ == '__main__':
  unittest.main()