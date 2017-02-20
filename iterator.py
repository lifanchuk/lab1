class Iterator(object):
    def __init__(self, Value):
        self.Index = 0
        self.Value = Value
    def __iter__(self):
        return self
    def __next__(self):
        if self.Index < self.Value:
            Index = self.Index
            self.Index += 1
            return Index
        else:
            raise StopIteration()

iter = Iterator(3)
for start in iter:
    print(start)

