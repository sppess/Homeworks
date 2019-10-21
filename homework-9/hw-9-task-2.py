# Write a class Product that has 4 attributes:
#   - type
#   - name
#   - price
#   - quantity

# and the following methods:
#   - add(amount) - adds a specified quantity of a single product
#   - set_discount(percent) - adds a discount for current product.
# discount must be specified in percentage


class Product:
    def __init__(self, type_, name, price, quantity):
        self.type = type_
        self.name = name
        self.price = price
        self.quantity = quantity

    def add(self, amount):
        self.quantity += amount

    def set_discount(self, percent):
        # self.discount = percent/100
        # self.price_d = self.price * self.discount
        # self.price = self.price - self.price_d
        self.price -= self.price * (self.price//100)


p = Product('Sport', 'Football T-Shirt', 100, 30)

assert p.quantity == 30
p.add(90)
assert p.quantity == 120

assert p.price == 100
p.set_discount(25)
assert p.price == 75
