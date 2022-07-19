class Even:
    def __init__(self, max):
        self.n = 2
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.max:
            result = self.n
            self.n += 2
            return result
        else:
            raise StopIteration


numbers = Even(20)
values = iter(numbers)
# for elements in values:
#     print(elements)


while (True):
    try:
        element = next(values)
        print(element)
    except StopIteration:
        break
