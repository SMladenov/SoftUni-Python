#Vehicle

class Vehicle:
    def __init__ (self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None
    def buy (self, money, owner):
        if self.price <= money and self.owner is None:
            self.owner = owner
            return f"Successfully bought a {self.type}. Change: {(money - self.price):.2f}"
        elif self.price > money:
            return f"Sorry, not enough money"
        elif self.owner is not None:
            return f"Car already sold"
    def sell (self):
        if self.owner is not None:
            self.owner = None
        else:
            return f"Vehicle has no owner"
    def __repr__ (self):
        if self.owner is not None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"
        