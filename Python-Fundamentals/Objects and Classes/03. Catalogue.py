#Catalogue

class Catalogue:
    def __init__ (self, name):
        self.name = name
        self.products = []

    def add_product (self, name):
        self.products.append(name)
    def get_by_letter (self, letter):
        filtered = [i for i in self.products if i.startswith(letter)]
        return filtered
    def __repr__ (self):
        sortedProducts = sorted(self.products)
        return f"Items in the {self.name} catalogue:\n" + '\n'.join(sortedProducts)
    