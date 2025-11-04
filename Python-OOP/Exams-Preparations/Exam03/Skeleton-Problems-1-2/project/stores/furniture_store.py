from project.stores.base_store import BaseStore
from collections import defaultdict

class FurnitureStore(BaseStore):
    def __init__(self, name, location):
        super().__init__(name, location, 50)
    
    @property
    def store_type(self):
        return "FurnitureStore"
    
  
    def store_stats(self):
        store_info = f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}"
        profit_info = self.get_estimated_profit()

        product_count = defaultdict(list)
        for product in self.products:
            product_count[product.model].append(product.price)

        sorted_models = sorted(product_count.keys())

        product_lines = ["**Furniture for sale:"]
        for model in sorted_models:
            num_pieces = len(product_count[model])
            avg_price = sum(product_count[model]) / num_pieces
            product_lines.append(f"{model}: {num_pieces}pcs, average price: {avg_price:.2f}")

        return f"{store_info}\n{profit_info}\n" + "\n".join(product_lines)


        