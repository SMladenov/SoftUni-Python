from project.dvd import DVD
from project.customer import Customer

class MovieWorld:
    def __init__ (self, name: str):
        self.name = name
        self.customers: list [Customer] = []
        self.dvds: list [DVD] = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10
    
    def add_customer (self, customer: Customer):
        if len(self.customers) < 10:
            self.customers.append(customer)
    
    def add_dvd (self, dvd: DVD):
        if len(self.dvds) < 15:
            self.dvds.append(dvd)
    
    def rent_dvd (self, customer_id: int, dvd_id: int):
        customerList = [customer for customer in self.customers if customer_id == customer.id]
        customer = customerList[0]

        if dvd_id in [dvd.id for dvd in customer.rented_dvds]:
            nameDvd = [dvd.name for dvd in customer.rented_dvds if dvd_id == dvd.id]
            return f"{customer.name} has already rented {nameDvd[0]}"
        
        #Check if DVD is rented by someone else
        otherCustomersDVD = [customer.rented_dvds for customer in self.customers if customer_id != customer.id]
        for listDvd in otherCustomersDVD:
            for dvd in listDvd:
                if dvd.id == dvd_id:
                    return "DVD is already rented"
        
        #Check if the customer has enough age
        dvdToBeRented = [dvd for dvd in self.dvds if dvd.id == dvd_id]
        if dvdToBeRented[0].age_restriction > customer.age:
            return f"{customer.name} should be at least {dvdToBeRented[0].age_restriction} to rent this movie"
        else:
            dvdToBeRented[0].is_rented = True
            customer.rented_dvds.append(dvdToBeRented[0])
            return f"{customer.name} has successfully rented {dvdToBeRented[0].name}"
        
    def return_dvd (self, customer_id: int, dvd_id: int):
        customerList = [customer for customer in self.customers if customer_id == customer.id]
        customer = customerList[0]

        if dvd_id in [dvd.id for dvd in customer.rented_dvds]:
            currentDVDList = [dvd for dvd in customer.rented_dvds if dvd_id == dvd.id]
            currentDVDList[0].is_rented = False
            customer.rented_dvds.remove(currentDVDList[0])
            return f"{customer.name} has successfully returned {currentDVDList[0].name}"
        else:
            return f"{customer.name} does not have that DVD"

    def __repr__ (self):
        listToOutput = []

        for customer in self.customers:
            listDVDNames = [dvd.name for dvd in customer.rented_dvds]
            listToOutput.append(f"{customer.id}: {customer.name} of age {customer.age} has {len(customer.rented_dvds)} rented DVD's ({', '.join(listDVDNames)})")
        
        for dvd in self.dvds:
            status = ""
            if dvd.is_rented:
                status = "rented"
            else:
                status = "not rented"

            listToOutput.append(f"{dvd.id}: {dvd.name} ({dvd.creation_month} {dvd.creation_year}) has age restriction {dvd.age_restriction}. Status: {status}")
        return '\n'.join(listToOutput)
    


