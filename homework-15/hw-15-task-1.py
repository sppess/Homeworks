# Extend the existing @logger decorator which writes logs to a file
# called log.txt instead of console

from functools import wraps


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with open("log.txt", "a") as file:
            file.write(func(*args, **kwargs) + '\n')
    return wrapper


@logger
def test_func(something):
    return something

test_func("first test")
test_func("second test")
