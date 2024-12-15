
def count_words(text):
    """Counts the number of words in a string."""
    words = text.split()
    return len(words)


def reverse_string(text):
    """Reverses the characters in a string."""
    return text[::-1]


def is_palindrome(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]
