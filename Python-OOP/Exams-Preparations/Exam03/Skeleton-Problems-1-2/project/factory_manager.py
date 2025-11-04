from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore
from collections import defaultdict

class FactoryManager():
    def __init__ (self, name: str):
        self.name = name
        self.income: float = 0.0
        self.products: list[BaseProduct] = []
        self.stores: list[BaseStore] = []
    
    def produce_item (self, product_type: str, model: str, price: float):
        if product_type != "Chair" and product_type != "HobbyHorse":
            raise Exception("Invalid product type!")
        
        if product_type == "Chair":
            newProd = Chair(model, price)
            self.products.append(newProd)
            return f"A product of sub-type {newProd.sub_type} was produced."
        elif product_type == "HobbyHorse":
            newProd2 = HobbyHorse(model, price)
            self.products.append(newProd2)
            return f"A product of sub-type {newProd2.sub_type} was produced."

    def register_new_store (self, store_type: str, name: str, location: str):
        if store_type != "FurnitureStore" and store_type != "ToyStore":
            raise Exception(f"{store_type} is an invalid type of store!")
        
        if store_type == "FurnitureStore":
            newStore = FurnitureStore(name, location)
            self.stores.append(newStore)
        elif store_type == "ToyStore":
            newStore2 = ToyStore(name, location)
            self.stores.append(newStore2)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store (self, store: BaseStore, *products: BaseProduct):
        if len(products) > store.capacity:
            return f"Store {store.name} has no capacity for this purchase."
        
        store_product_type = "Furniture" if isinstance(store, FurnitureStore) else "Toys"

        suitable_products = [product for product in products if product.sub_type == store_product_type]

        if not suitable_products:
            return f"Products do not match in type. Nothing sold."
        
        for product in suitable_products:
            if product in self.products:
                self.products.remove(product)
        
        store.products.extend(suitable_products)
        store.capacity -= len(suitable_products)

        total_price = sum([product.price for product in suitable_products])
        self.income += total_price

        return f"Store {store.name} successfully purchased {len(suitable_products)} items."
    
    def unregister_store (self, store_name: str):
        storeFound = [store for store in self.stores if store.name == store_name]
        if not storeFound:
            raise Exception("No such store!")
        if storeFound[0].products:
            return f"The store is still having products in stock! Unregistering is inadvisable."
        
        self.stores.remove(storeFound[0])
        return f"Successfully unregistered store {store_name}, location: {storeFound[0].location}."
    
    def discount_products (self, product_model: str):
        matching_products = [product for product in self.products if product.model == product_model]
        if not matching_products:
            return f"Discount applied to 0 products with model: {product_model}"
        
        for product in matching_products:
            product.discount()
        
        return f"Discount applied to {len(matching_products)} products with model: {product_model}"

    def request_store_stats (self, store_name: str):
        storeFound = [store for store in self.stores if store.name == store_name]

        if storeFound:
            return f"{storeFound[0].store_stats()}"
        else:
            return f"There is no store registered under this name!"
        
    def statistics(self):
        factory_income = f"{self.income:.2f}"
        product_count_dict = {}
        total_price = 0

        for product in self.products:
            if product.model not in product_count_dict:
                product_count_dict[product.model] = 0
            product_count_dict[product.model] += 1
            total_price += product.price
        
        total_products = sum(product_count_dict.values())
        formatted_total_price = f"{total_price:.2f}"

        sorted_products = sorted(product_count_dict.items())
        product_stats = "\n".join(f"{model}: {count}" for model, count in sorted_products)

        sorted_stores = sorted(store.name for store in self.stores)
        store_stats = "\n".join(sorted_stores)

        return (
        f"Factory: {self.name}\n"
        f"Income: {factory_income}\n"
        f"***Products Statistics***\n"
        f"Unsold Products: {total_products}. Total net price: {formatted_total_price}\n"
        f"{product_stats}\n"
        f"***Partner Stores: {len(self.stores)}***\n"
        f"{store_stats}"
        )

# # Initialize the FactoryManager
# factory_manager = FactoryManager("Cool Factory")
# # Produce some items
# print(factory_manager.produce_item("Chair", "Classic", 80.0))
# print(factory_manager.produce_item("Chair", "Modern", 100.0))
# print(factory_manager.produce_item("Chair", "Modern", 200.0))
# print(factory_manager.produce_item("HobbyHorse", "Rocking Horse", 120.0))
# print(factory_manager.produce_item("HobbyHorse", "Rocking Horse", 100.0))
# print()
# # Register new stores
# print(factory_manager.register_new_store("FurnitureStore", "Furniture Outlet", "SOF"))
# print(factory_manager.register_new_store("ToyStore", "Toy World", "VAR"))
# print()
# # Sell products to stores
# chair1 = factory_manager.products[0]
# chair2 = factory_manager.products[1]
# chair3 = factory_manager.products[2]
# store1 = factory_manager.stores[0]
# store2 = factory_manager.stores[1]
# print(factory_manager.sell_products_to_store(store2, chair1, chair2))
# print(factory_manager.sell_products_to_store(store1, chair1, chair2, chair3))
# print()
# # Unregister store
# print(factory_manager.unregister_store("Furniture Outlet"))
# print()
# # Discount products
# print(factory_manager.discount_products("Classic"))
# print(factory_manager.discount_products("Rocking Horse"))
# print()
# # Request store statistics
# print(factory_manager.request_store_stats("Furniture Outlet"))
# print(factory_manager.request_store_stats("Toy World"))
# print()
# # Factory statistics
# print(factory_manager.statistics())
# print()
# # Unregister store
# print(factory_manager.unregister_store("Toy World"))



