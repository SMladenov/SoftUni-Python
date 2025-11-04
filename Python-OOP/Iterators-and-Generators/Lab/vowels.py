class vowels:
    def __init__ (self, someString: str):
        self.someString = someString
        self.vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'u', 'U', 'y', 'Y', 'o', 'O']
        self.startIndex = -1

    def __iter__ (self):
        return self

    def __next__ (self):
        
        while True:
            self.startIndex += 1

            if self.startIndex >= len(self.someString):
                raise StopIteration()    
            if self.someString[self.startIndex] in self.vowels:
                    return self.someString[self.startIndex]
            
my_string = vowels('Abcedifuty0o')

for char in my_string:

    print(char)