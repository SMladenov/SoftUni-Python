class reverse_iter:
    def __init__ (self, someList: list):
        self.someList = someList
        self.startIndex = len(self.someList)

    def __iter__ (self):
        return self
    
    def __next__ (self):

        self.startIndex -= 1

        if self.startIndex >= 0:
            return self.someList[self.startIndex]
        raise StopIteration()

reversed_list = reverse_iter([1, 2, 3, 4])

for item in reversed_list:

    print(item)