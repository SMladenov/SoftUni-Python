from project.product import Product
# from project.drink import Drink
# from project.food import Food

class ProductRepository:
    def __init__ (self):
        self.products: list[Product] = []

    def add (self, product: Product):
        self.products.append(product)
    
    def find (self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product
    
    def remove (self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                return
    
    def __repr__ (self):
        listToOutput = []
        for product in self.products:
            listToOutput.append(f"{product.name}: {product.quantity}")
        return '\n'.join(listToOutput)
    
# food = Food("apple")

# drink = Drink("water")

# repo = ProductRepository()

# repo.add(food)

# repo.add(drink)

# print(repo.products)

# print(repo.find("water"))

# repo.find("apple").decrease(5)

# print(repo)
