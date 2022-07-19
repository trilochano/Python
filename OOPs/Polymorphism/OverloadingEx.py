class A:

    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c


a = A()
print(a.add(1,8,)) # TypeError: add() missing 1 required positional argument: 'c'
