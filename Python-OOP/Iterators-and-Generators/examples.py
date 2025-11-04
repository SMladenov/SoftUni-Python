class Person:
    def __init__ (self, name):
        self.name = name
        self.current_index = -1

    def __len__ (self):
        return len(self.name)
    
    # def __iter__ (self):
    #     return self
    
    def __iter__ (self):
        return iter(self.name)
    
    # def __next__ (self):
    #     self.current_index += 1
    #     if self.current_index < len(self.name):
    #         return self.name[self.current_index]
    #     raise StopIteration()
    
p = Person("Test")
print(len(p))

for el in p:
    print(el)

#Generators

def first_n(n):
    num = 0
    while num < n:
        yield num #yield passes the num value to the below for loop when called
        num += 1

result = first_n(5)
print (result)
for el in result:
    print (el)
