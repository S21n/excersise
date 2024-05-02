def is_palindrome(s):
    """
    Check if a string is a palindrome.

    A palindrome is a word, phrase, number, or other sequence of characters
    that reads the same forward and backward, ignoring spaces, punctuation,
    and capitalization.

    Parameters
    ----------
    s : str
        The string to check for palindrome property.

    Returns
    -------
    bool
        True if the string is a palindrome, False otherwise.

    """
    # Remove any non-alphanumeric characters and convert to lowercase
    s = ''.join(c.lower() for c in s if c.isalnum()).strip()

    # Base case: empty string or single character is a palindrome
    if not s or len(s) == 1:
        return True

    # Compare the first and last characters
    if s[0] != s[-1]:
        return False

    # Recursively check the rest of the string
    return is_palindrome(s[1:-1])


string = "amma"
print(f"Is '{string}' a palindrome? - {is_palindrome(string)}")