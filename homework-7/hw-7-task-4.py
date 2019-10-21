# Write a function that takes 2 dictionaries where keys are cars and values
# are their prices. The function checks whether the sum of prices in 1
# dictionary is equal to the sum in the 2nd


def compare_prices(dict1: dict, dict2: dict) -> bool:
    return sum(dict1.values()) == sum(dict2.values())


assert compare_prices({'BMW': 20000, 'Nissan': 15000},
                      {'Mustang': 30000, 'Renault': 5000}) is True
assert compare_prices({'Volvo': 13000, 'Infinity': 80000},
                      {'Ford GT': 100000, 'Lada': 3000}) is False
