# Write a function using list comprehensions that takes a string and changes
# letter's case from upper to lower and vice versa


def change_case(string):

    return ''.join([letter.upper() if letter.islower()
                    else letter.lower() for letter in string])


def change_case1(string) -> str:
    return ''.join(letter.swapcase() for letter in string)


assert change_case1("HELLO") == "hello"
assert change_case1("Hi! I'm Jim :)") == "hI! i'M jIM :)"
assert change_case1("welcome y'all") == "WELCOME Y'ALL"
