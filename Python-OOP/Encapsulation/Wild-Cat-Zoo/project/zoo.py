from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__ (self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: list[Animal] = []
        self.workers: list[Worker] = []
    
    def add_animal (self, animal: Animal, price: int):
        if self.__budget - price >= 0 and self.__animal_capacity > 0:
            self.__budget -= price
            self.__animal_capacity -= 1
            self.animals.append(animal)
            return f"{animal.name} the {type(animal).__name__} added to the zoo"

        elif self.__animal_capacity > 0 and self.__budget - price < 0:
            return f"Not enough budget"
        else:
            return f"Not enough space for animal"
    
    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > 0:
            self.__workers_capacity -= 1
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        else:
            return f"Not enough space for worker"
    
    def fire_worker (self, worker_name: str):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                self.__workers_capacity += 1
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers (self):
        allSalaries = sum([worker.salary for worker in self.workers])
        if self.__budget - allSalaries >= 0:
            self.__budget -= allSalaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return f"You have no budget to pay your workers. They are unhappy"
    
    def tend_animals (self):
        allMoneyForCare = sum([animal.money_for_care for animal in self.animals])
        if self.__budget - allMoneyForCare >= 0:
            self.__budget -= allMoneyForCare
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            return f"You have no budget to tend the animals. They are unhappy."
    
    def profit (self, amount: int):
        self.__budget += amount
    
    def animals_status (self):
        listToOutput = []
        listToOutput.append(f"You have {len(self.animals)} animals")
        listLions = [animal for animal in self.animals if type(animal).__name__ == "Lion"]
        listTigers = [animal for animal in self.animals if type(animal).__name__ == "Tiger"]
        listCheetahs = [animal for animal in self.animals if type(animal).__name__ == "Cheetah"]
        listToOutput.append(f"----- {len(listLions)} Lions:")
        if listLions:
            for animal in listLions:
                listToOutput.append(f"Name: {animal.name}, Age: {animal.age}, Gender: {animal.gender}")

        listToOutput.append(f"----- {len(listTigers)} Tigers:")
        if listTigers:
            for animal in listTigers:
                listToOutput.append(f"Name: {animal.name}, Age: {animal.age}, Gender: {animal.gender}")

        listToOutput.append(f"----- {len(listCheetahs)} Cheetahs:")
        if listCheetahs:
            for animal in listCheetahs:
                listToOutput.append(f"Name: {animal.name}, Age: {animal.age}, Gender: {animal.gender}")
        return '\n'.join(listToOutput)

    def workers_status (self):
        listToOutput = []
        listToOutput.append(f"You have {len(self.workers)} workers")
        listKeepers = [worker for worker in self.workers if type(worker).__name__ == "Keeper"]
        listCaretaker = [worker for worker in self.workers if type(worker).__name__ == "Caretaker"]
        listVets = [worker for worker in self.workers if type(worker).__name__ == "Vet"]

        listToOutput.append(f"----- {len(listKeepers)} Keepers:")
        if listKeepers:
            for keeper in listKeepers:
                listToOutput.append(f"Name: {keeper.name}, Age: {keeper.age}, Salary: {keeper.salary}")

        listToOutput.append(f"----- {len(listCaretaker)} Caretakers:")
        if listCaretaker:
            for caretaker in listCaretaker:
                listToOutput.append(f"Name: {caretaker.name}, Age: {caretaker.age}, Salary: {caretaker.salary}")

        listToOutput.append(f"----- {len(listVets)} Vets:")
        if listVets:
            for vet in listVets:
                listToOutput.append(f"Name: {vet.name}, Age: {vet.age}, Salary: {vet.salary}")
        return '\n'.join(listToOutput)