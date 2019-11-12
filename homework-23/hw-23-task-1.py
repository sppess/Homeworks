# Write a function is_palindrome which takes a string and returns boolean
# whether the string is a palindrome or not


def is_palindrome(word: str) -> bool:
    if word[0] != word[-1]:
        return False
    if len(word) <= 2:
        return True
    return is_palindrome(word[1:-1])
