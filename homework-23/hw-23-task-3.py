# Write a function first_letter which takes a string and returns first
# uppercase letter in it


def first_letter(string: str) -> str:
    print(string)
    if string[0].isupper():
        return string[0]
    return first_letter(string[1:])
