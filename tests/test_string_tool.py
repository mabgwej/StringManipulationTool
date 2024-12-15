import unittest
from string_tool.main import count_words, reverse_string, is_palindrome


class TestStringFunctions(unittest.TestCase):

    def test_count_words(self):
        self.assertEqual(count_words("Hello world!"), 2)
        self.assertEqual(count_words("This is a test."), 4)
        self.assertEqual(count_words(""), 0)  # Edge case: empty string
        self.assertEqual(count_words("SingleWord"), 1)  # Single word test

    def test_reverse_string(self):
        self.assertEqual(reverse_string("Hello"), "olleH")
        self.assertEqual(reverse_string("Python"), "nohtyP")
        self.assertEqual(reverse_string(""), "")  # Edge case: empty string
        self.assertEqual(reverse_string("A man"), "nam A")  # Space handling

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(is_palindrome("Hello"))
        self.assertTrue(
            is_palindrome("No 'x' in Nixon")
        )  # Palindrome with punctuation
        self.assertTrue(is_palindrome(""))  # Edge case: empty string


if __name__ == "__main__":
    unittest.main()
