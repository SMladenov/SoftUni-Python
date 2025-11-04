from project.clients.base_client import BaseClient
from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.base_waiter import BaseWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter

class SphereRestaurantApp():
    def __init__ (self):
        self.waiters: list[BaseWaiter] = []
        self.clients: list[BaseClient] = []
    
    def hire_waiter (self, waiter_type: str, waiter_name: str, hours_worked: int):
        if waiter_type not in ["FullTimeWaiter", "HalfTimeWaiter"]:
            return f"{waiter_type} is not a recognized waiter type."

        if waiter_name in [waiter.name for waiter in self.waiters if waiter.name == waiter_name]:
            return f"{waiter_name} is already on the staff."

        if waiter_type == "FullTimeWaiter":
            waiter = FullTimeWaiter(waiter_name, hours_worked)
            self.waiters.append(waiter)
        elif waiter_type == "HalfTimeWaiter":
            waiter = HalfTimeWaiter(waiter_name, hours_worked)
            self.waiters.append(waiter)
        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client (self, client_type: str, client_name: str):
        if client_type not in ["RegularClient", "VIPClient"]:
            return f"{client_type} is not a recognized client type."
        
        if client_name in [client.name for client in self.clients if client_name == client.name]:
            return f"{client_name} is already a client."
        
        if client_type == "RegularClient":
            client = RegularClient(client_name)
            self.clients.append(client)
        elif client_type == "VIPClient":
            client = VIPClient(client_name)
            self.clients.append(client)
        return f"{client_name} is successfully admitted as a {client_type}."
    
    def process_shifts (self, waiter_name: str):
        waiterFound = [waiter for waiter in self.waiters if waiter.name == waiter_name]
        if waiterFound:
            return waiterFound[0].report_shift()
        else:
            return f"No waiter found with the name {waiter_name}."
    
    def process_client_order (self, client_name: str, order_amount: float):
        clientFound = [client for client in self.clients if client.name == client_name]
        if clientFound:
            return f"{client_name} earned {int(clientFound[0].earning_points(order_amount))} points from the order."
        else:
            return f"{client_name} is not a registered client."

    def apply_discount_to_client (self, client_name: str):
        clientFound = [client for client in self.clients if client.name == client_name]
        if clientFound:
            discountTuple = clientFound[0].apply_discount()
            return f"{client_name} received a {discountTuple[0]}% discount. Remaining points {int(clientFound[0].points)}"
        else:
            return f"{client_name} cannot get a discount because this client is not admitted!"

    def generate_report (self):
        listToOutput = []
        total_earnings = sum(waiter.calculate_earnings() for waiter in self.waiters)
        total_client_points = sum(client.points for client in self.clients)
        clients_count = len(self.clients)

        sorted_waiters = sorted(self.waiters, key=lambda w: w.calculate_earnings(), reverse=True)

        listToOutput.append("$$ Monthly Report $$")
        listToOutput.append(f"Total Earnings: ${total_earnings:.2f}")
        listToOutput.append(f"Total Clients Unused Points: {int(total_client_points)}")
        listToOutput.append(f"Total Clients Count: {clients_count}")
        listToOutput.append("** Waiter Details **")

        for waiter in sorted_waiters:
            listToOutput.append(f"Name: {waiter.name}, Total earnings: ${waiter.calculate_earnings():.2f}")

        return "\n".join(listToOutput)


# # Create an instance of SphereRestaurantApp
# sphere_restaurant_app = SphereRestaurantApp()

# # Hire some waiters
# print(sphere_restaurant_app.hire_waiter("FullTimeWaiter", "John", 40))
# print(sphere_restaurant_app.hire_waiter("HalfTimeWaiter", "Alice", 20))
# print(sphere_restaurant_app.hire_waiter("InvalidWaiter", "JohnDoe", 10))
# print(sphere_restaurant_app.hire_waiter("HalfTimeWaiter", "Charlie", 30))
# print(sphere_restaurant_app.hire_waiter("FullTimeWaiter", "Frank", 50))
# print(sphere_restaurant_app.hire_waiter("HalfTimeWaiter", "Alice", 60))

# # Admit some clients
# print(sphere_restaurant_app.admit_client("InvalidClient", "JohnDoe"))
# print(sphere_restaurant_app.admit_client("VIPClient", "Eve"))
# print(sphere_restaurant_app.admit_client("VIPClient", "Lila"))
# print(sphere_restaurant_app.admit_client("RegularClient", "Bob"))
# print(sphere_restaurant_app.admit_client("VIPClient", "Eve"))
# print(sphere_restaurant_app.admit_client("RegularClient", "Oscar"))

# # Process shifts
# print(sphere_restaurant_app.process_shifts("John"))
# print(sphere_restaurant_app.process_shifts("Alice"))
# print(sphere_restaurant_app.process_shifts("Emily"))
# print(sphere_restaurant_app.process_shifts("Frank"))

# # Process client orders
# print(sphere_restaurant_app.process_client_order("Bob", 100.0))
# print(sphere_restaurant_app.process_client_order("Eve", 500.0))
# print(sphere_restaurant_app.process_client_order("JohnDoe", 250.0))
# print(sphere_restaurant_app.process_client_order("Bob", 750.0))
# print(sphere_restaurant_app.process_client_order("Lila", 550.0))
# print(sphere_restaurant_app.process_client_order("Oscar", 84.0))

# # Apply discounts to clients
# print(sphere_restaurant_app.apply_discount_to_client("Lila"))
# print(sphere_restaurant_app.apply_discount_to_client("Eve"))
# print(sphere_restaurant_app.apply_discount_to_client("JohnDoe"))
# print(sphere_restaurant_app.apply_discount_to_client("Oscar"))
# print(sphere_restaurant_app.apply_discount_to_client("Bob"))

# # Generate report
# print(sphere_restaurant_app.generate_report())
