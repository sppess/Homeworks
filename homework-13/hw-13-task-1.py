from functools import wraps
# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!
# For example:
#   "add called with 4, 5"


def logger(func):
    def wripper(*args, **kwargs):
        arguments = ''
        for arg in args:
            arguments += f"{arg}, "
        return f"{func.__name__} called with {arguments[0:-2]}"
        # new_str = ', '.join([arg for arg in args])
        # return f"{func.__name__} called with {new_str}"
    return wripper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

print(add(3, 6))
