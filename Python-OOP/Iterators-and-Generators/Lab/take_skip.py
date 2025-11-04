class take_skip:
    def __init__ (self, pace: int, times: int):
        self.pace = pace
        self.times = times
        self.current_time = 0
        self.current_value = 0

    
    def __iter__ (self):
        return self
    
    def __next__ (self):

        if self.current_time >= self.times:
            raise StopIteration()

        valueToReturn = self.current_value
        
        self.current_value += self.pace
        self.current_time += 1
        return valueToReturn

numbers = take_skip(5, 1)

for number in numbers:

    print(number)

# numbers = take_skip(10, 5)

# for number in numbers:

#     print(number)