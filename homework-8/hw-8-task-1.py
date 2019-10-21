# Write a custom sum function that takes any number of arguments and returns
# their sum. If the number of arguments is more than 20, return None instead


def custom_sum(*args) -> int:
    if len(args) < 20:
        return sum(args)


def cust_sum(*args):
    return sum(args) if len(args) < 20 else None


assert custom_sum(12, 12, 13) == 37
assert custom_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                  11, 12, 13, 14, 15, 16, 17, 18, 19, 20) is None
