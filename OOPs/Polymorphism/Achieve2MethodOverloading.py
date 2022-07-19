# By Using Multiple Dispatch Decorator

from multipledispatch import dispatch


class A:

    @dispatch(int, int)
    def add(self, first, second):
        return first + second

    @dispatch(int, int, int)
    def add(self, first, second, third):
        return first + second + third

    @dispatch(float, float)
    def add(self, first, second):
        return first + second


a = A()
print(a.add(1, 2))
print(a.add(1, 2,3))
print(a.add(20.90, 89.0))
