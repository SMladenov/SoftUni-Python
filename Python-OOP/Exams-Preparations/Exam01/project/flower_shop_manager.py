from project.clients.base_client import BaseClient
from project.plants.base_plant import BasePlant
from project.plants.flower import Flower
from project.plants.leaf_plant import LeafPlant
from project.clients.business_client import BusinessClient
from project.clients.regular_client import RegularClient

class FlowerShopManager:
    def __init__ (self):
        self.income: float = 0.0
        self.plants: list[BasePlant] = []
        self.clients: list[BaseClient] = []

    def add_plant(self, plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int, plant_extra_data: str):
        if plant_type == "Flower":
            addedFlower = Flower(plant_name, plant_price, plant_water_needed, plant_extra_data)
            self.plants.append(addedFlower)
            return f"{plant_name} is added to the shop as {plant_type}."
        elif plant_type == "LeafPlant":
            addedFlower = LeafPlant(plant_name, plant_price, plant_water_needed, plant_extra_data)
            self.plants.append(addedFlower)
            return f"{plant_name} is added to the shop as {plant_type}."
        else:
            raise ValueError("Unknown plant type!")
        
    def add_client (self, client_type: str, client_name: str, client_phone_number: str):
        if client_type == "RegularClient":
            listDuplicatePhone = [client for client in self.clients if client.phone_number == client_phone_number]
            if listDuplicatePhone:
                raise ValueError("This phone number has been used!")
            else:
                addedClient = RegularClient(client_name, client_phone_number)
                self.clients.append(addedClient)
                return f"{client_name} is successfully added as a {client_type}."
            
        elif client_type == "BusinessClient":
            listDuplicatePhone = [client for client in self.clients if client.phone_number == client_phone_number]
            if listDuplicatePhone:
                raise ValueError("This phone number has been used!")
            else:
                addedClient = BusinessClient(client_name, client_phone_number)
                self.clients.append(addedClient)
                return f"{client_name} is successfully added as a {client_type}."
            
        else:
            raise ValueError("Unknown client type!")
        

    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):
        foundClient = [client for client in self.clients if client.phone_number == client_phone_number]
        if not foundClient:
            raise ValueError("Client not found!")
        
        available_quantity = sum(1 for plant in self.plants if plant.name == plant_name)
        #foundPlant = [plant for plant in self.plants if plant.name == plant_name]
        if available_quantity <= 0:
            raise ValueError("Plants not found!")
        
        if available_quantity < plant_quantity:
            return f"Not enough plant quantity."
        
        totalPrice = 0
        #Remove sold plants
        for _ in range (plant_quantity):
            for plant in self.plants:
                if plant.name == plant_name:
                    currentDiscount = plant.price * (foundClient[0].discount / 100)
                    currentPrice = plant.price - currentDiscount
                    totalPrice += currentPrice
                    self.plants.remove(plant)
                    break
        
        foundClient[0].update_total_orders()
        foundClient[0].update_discount()
        
        self.income += totalPrice
        return f"{plant_quantity}pcs. of {plant_name} plant sold for {totalPrice:.2f}"


    def remove_plant(self, plant_name: str):
        foundPlant = [plant for plant in self.plants if plant.name == plant_name]
        if not foundPlant:
            return f"No such plant name."
        
        for plant in self.plants:
            if plant.name == plant_name:
                self.plants.remove(plant)
                return f"Removed {plant.plant_details()}"
    
    def remove_clients (self):
        clientsRemoved = 0
        clients_copy = self.clients.copy()
        for client in clients_copy:
            if client.total_orders == 0:
                self.clients.remove(client)
                clientsRemoved += 1

        return f"{clientsRemoved} client/s removed."

    def shop_report (self):
        listToOutput = []

        plantsDict = {}
        for plant in self.plants:
            if plant.name not in plantsDict.keys():
                plantsDict[plant.name] = 1
            else:
                plantsDict[plant.name] += 1

        # Sort plants first by the count (descending), then by name (ascending)
        sorted_plants = sorted(plantsDict.items(), key=lambda x: (-x[1], x[0]))

        total_orders = sum(client.total_orders for client in self.clients)
        listToOutput.append(f"~Flower Shop Report~\nIncome: {self.income:.2f}\nCount of orders: {total_orders}\n~~Unsold plants: {len(self.plants)}~~")
        for plant_name, count in sorted_plants:
            listToOutput.append(f"{plant_name}: {count}")
        
        #Time for the Clients
        listToOutput.append(f"~~Clients number: {len(self.clients)}~~")
        sorted_clients = sorted(self.clients, key=lambda c: (-c.total_orders, c.phone_number))
        for client in sorted_clients:
            listToOutput.append(client.client_details())

        return "\n".join(listToOutput)


