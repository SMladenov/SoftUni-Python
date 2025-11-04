class dictionary_iter:
    def __init__ (self, randomDict: dict):
        self.randomDict = list(randomDict.items())
        self.current_index = 0
    
    def __iter__ (self):
        return self
    
    def __next__ (self):

        if self.current_index == len(self.randomDict):
            raise StopIteration()
    
        result = self.randomDict[self.current_index]
        self.current_index += 1
        return result

result = dictionary_iter({1: "1", 2: "2"})

for x in result:

    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})

for x in result:

    print(x)

       
            