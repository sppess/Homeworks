x = int(input("x = "))
y = int(input("y = "))
operation = input("Choose the operation "
                  "(sum, dif, div, f-div, multi, pow, %): ")


def calculate(x, y, operation):
    key = operation

    calc = {
        'sum': x + y,
        'dif': x - y,
        'dev': x / y,
        'f-div': x // y,
        'multi': x * y,
        'pow': x ** y,
        '%': x % y
    }

    return calc[key]


print(calculate(x, y, operation))
