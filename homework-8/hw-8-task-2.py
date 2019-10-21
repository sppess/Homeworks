# Write a function that takes a list of strings and removes those strings
# that don't consist of unique letters


def remove_string_doubles(strings: list) -> list:
    return [word for word in strings if len(word) == len(set(word))]


assert remove_string_doubles(['cat', 'escape', 'template', 'head']) == \
       ['cat', 'head']
assert remove_string_doubles(['lamp', 'hash']) == ['lamp']
