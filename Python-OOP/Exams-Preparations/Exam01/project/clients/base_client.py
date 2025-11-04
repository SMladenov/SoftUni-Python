from abc import ABC, abstractmethod

class BaseClient (ABC):
    def __init__(self, name: str, phone_number: str):
        self.name = name
        self.phone_number = phone_number
        self.discount = 0.0
        self.total_orders = 0
    
    @property
    def name (self):
        return self.__name
    @name.setter
    def name (self, name: str):
        nameStrip = name.strip()
        if len(nameStrip) < 2:
            raise ValueError("Name must be at least two characters long!")
        else:
            self.__name = nameStrip
    
    @property
    def phone_number (self):
        return self.__phone_number
    @phone_number.setter
    def phone_number (self, phone_number: str):
        
        for _ in phone_number:
            if not _.isdigit():
                raise ValueError("Phone number can contain only digits!")
        self.__phone_number = phone_number

    @property
    def discount (self):
        return self.__discount
    @discount.setter 
    def discount (self, discount: float):
        self.__discount = discount
    
    @property
    def total_orders (self):
        return self.__total_orders
    @total_orders.setter
    def total_orders (self, total_orders: int):
        self.__total_orders = total_orders
    
    @abstractmethod
    def update_discount(self):
        pass

    def update_total_orders(self):
        self.total_orders += 1
    
    def client_details(self):
        return f"Client: {self.name}, Phone number: {self.phone_number}, Orders count: {self.total_orders}, Discount: {int(self.discount)}%"
    


        





# class Person:
#     def __init__ (self, age = 0):
#         self.age = age

#     #props Shortcut
#     @property
#     def age (self):
#         return self.__age
    
#     @age.setter
#     def age (self, age):
#         if age < 18:
#             self.__age = 18
#         else:
#             self.__age = age

    

# p = Person(2)
# print (p.age)