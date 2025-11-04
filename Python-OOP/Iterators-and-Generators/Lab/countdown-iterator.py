class countdown_iterator:
    def __init__ (self, count: int):
        self.count = count
    
    def __iter__ (self):
        return self
    
    def __next__ (self):

        currentNum = self.count
        if currentNum >= 0:
            self.count -= 1
            return currentNum
        raise StopIteration()

iterator = countdown_iterator(10)

for item in iterator:

    print(item, end=" ")

print()

iterator = countdown_iterator(0)

for item in iterator:

    print(item, end=" ")