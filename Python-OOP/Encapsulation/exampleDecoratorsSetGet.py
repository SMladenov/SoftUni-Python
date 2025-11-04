

class Person:
    def __init__ (self, age = 0):
        self.age = age

    #props Shortcut
    @property
    def age (self):
        return self.__age
    
    @age.setter
    def age (self, age):
        if age < 18:
            self.__age = 18
        else:
            self.__age = age

    

p = Person(2)
print (p.age)

print (getattr(p, 'age', None)) # -> if not found return None
print (hasattr(p, 'age'))
print (hasattr(p, 'asd'))
setattr(p, 'age', 37)
print (getattr(p, 'age', None))
