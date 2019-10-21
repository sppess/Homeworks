# Write a function that takes a sentence (string) and any number of
# key-word arguments. All kwargs are filters for that question.
# These filters decide whether the function returns True or False
# Possible filters:
#   - max_length: integer !REQUIRED FILTER
#   - includes: list of strings (substring that the sentence must contain)
#   - has_spaces: boolean
#   etc
#
# max_length is required kwarg. If it hasn't been provided, the function
# must return None
#
# see asserts for better understanding


def is_valid(string, **filters):

    if 'max_length' not in filters:
        return None

    if len(string) > filters:
        return False

    if any(s not in string for s in filters.get('includes', [])):
        return False

    if 'has_spaces' in filters:
        return ' ' in string

    return True


print(is_valid('Hey guys! Have you ever played football:)', includes=['?', '.'], max_length=100))

# assert is_valid('Hi! My name is Jim', max_length=30, has_spaces=True) is True
# assert is_valid('RobertSteveJohn', max_length=10, has_spaces=False) is False
# assert is_valid('Hey guys! Have you ever played football:)', includes=['?', '.'], max_length=100) is False
# assert is_valid("What's up?", has_spaces=True) is None
