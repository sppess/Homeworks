string = "SheWalksToTheBeach"


def insert_whitespace(string):
    new_string = ''

    for el in string:
        if el.isupper() and string.index(el) != 0:
            new_string += ' '
        new_string += el

    return new_string


print(insert_whitespace(string))
