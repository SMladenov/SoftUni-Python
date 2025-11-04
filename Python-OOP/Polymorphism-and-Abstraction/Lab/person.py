from abc import ABC, abstractmethod

class Person:
    def __init__ (self, name: str, surname: str):
        self.name = name
        self.surname = surname

    # def __eq__ (self, person):
    #     if isinstance(person, Person):
    #         return f"{self.name} {self.surname}"
    
    def __add__ (self, person):
        if isinstance(person, Person):
            return Person(self.name, person.surname)
    
    def __repr__ (self):
        return f"{self.name} {self.surname}"
        

class Group:
    def __init__ (self, name: str, people: list[Person]):
        self.name = name
        self.people = people

    def __len__ (self):
        return len(self.people)
    
    def __add__ (self, group):
        if isinstance(group, Group):
            return Group(f"{self.name} {group.name}", self.people + group.people)

    def __repr__ (self):
        peopleNames = [f"{people.name} {people.surname}" for people in self.people]
        return f"Group {self.name} with members {', '.join(peopleNames)}"
    
    def __getitem__ (self, index):
        if 0 <= index < len(self.people):
            return f"Person {index}: {self.people[index]}"
    
    def __iter__ (self):
        listToOutput = []
        for index, people in enumerate(self.people):
            listToOutput.append(f"Person {index}: {people.name} {people.surname}")
        
        return iter(listToOutput)
    

    
p0 = Person('Aliko', 'Dangote')

p1 = Person('Bill', 'Gates')

p2 = Person('Warren', 'Buffet')

p3 = Person('Elon', 'Musk')

p4 = p2 + p3


first_group = Group('__VIP__', [p0, p1, p2])

second_group = Group('Special', [p3, p4])

third_group = first_group + second_group

print(len(first_group))

print(second_group)

print(third_group[0])


for person in third_group:

    print(person)