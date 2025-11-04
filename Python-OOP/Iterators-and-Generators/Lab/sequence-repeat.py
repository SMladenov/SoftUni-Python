class sequence_repeat:
    def __init__ (self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.currentNumber = 0
        self.currentIndex = -1

    
    def __iter__ (self):
        return self
    
    def __next__ (self):

        if self.currentNumber == self.number:
            raise StopIteration()

        self.currentIndex += 1
        self.currentNumber += 1
        if self.currentIndex == len(self.sequence):
            self.currentIndex = 0
        return self.sequence[self.currentIndex]

result = sequence_repeat('abc', 5)

for item in result:

    print(item, end ='')

print()

result = sequence_repeat('I Love Python', 3)

for item in result:

    print(item, end ='')