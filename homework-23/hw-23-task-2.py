# Write a function copy_string which takes a string and recursively, character
# by character creates a copy of it.


def copy_string_v1(string: str, new_string='') -> str:
    if len(string) == 0:
        return new_string
    new_string += string[0]
    return copy_string_v1(string[1:], new_string)
    
