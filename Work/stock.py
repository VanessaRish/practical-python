class Stock:

    __slots__ = ['name', 'price', '_shares']

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"

    @property
    def cost(self):
        return self.shares * self.price

    @property
    def shares(self):
        return self._shares

    def sell(self, amount):
        self.shares -= amount
        return self.shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value,int):
            raise TypeError("Must be integer")
        self._shares = value


class MyStock(Stock):
    def __init__(self, name, shares, price, factor):
        super().__init__(name, shares, price)
        self.factor = factor

    def panic(self):
        self.sell(self.shares)

    def cost(self):
        return self.factor * super().cost()
