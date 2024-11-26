#Zoo

class Zoo:
    __animals = 0
    
    def __init__ (self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []
        
    def add_animal (self, species, name):
        if species == "mammal":
            self.mammals.append(name)
            Zoo.__animals += 1
        elif species == "fish":
            self.fishes.append(name)
            Zoo.__animals += 1
        elif species == "bird":
            self.birds.append(name)
            Zoo.__animals += 1
    def get_info (self, species):
        if species == "mammal":
            return f"Mammals in {self.name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}"
        elif species == "bird":
            return f"Birds in {self.name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}"
        elif species == "fish":
            return f"Fishes in {self.name}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals}"
        
name = input()
zoo = Zoo(name)
numbers = int(input())

for i in range (numbers):
    cmdSplit = input().split(' ')
    specie = cmdSplit[0]
    name = cmdSplit[1]
    zoo.add_animal(specie, name)
    
infoSpecie = input()
print (f"{zoo.get_info(infoSpecie)}")