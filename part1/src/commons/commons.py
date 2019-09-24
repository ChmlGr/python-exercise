def is_palindrome(phrase):
    cleaned = [c.casefold() for c in phrase if c.isalpha()]
    return cleaned == cleaned[::-1]