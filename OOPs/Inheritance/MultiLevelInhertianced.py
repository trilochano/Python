# class A:
#     def __init__(self):
#         print("A Class")
#
#
# class B(A):
#     def __init__(self):
#         print("B Class")
#
#
# class C(B):
#     def __init__(self):
#         super().__init__()
#         print("C Class")
#
#
# c = C()


class A:
    def __init__(self):
        print("A Class")

    def add(self, a, b):
        print(a + b)


class B(A):
    def __init__(self):
        print("B Class")

    def add(self, a, b):
        super().add(a, b)
        print(a - b)


class C(B):
    def __init__(self):
        A.__init__(self)
        print("C Class")

    def add(self, a, b):
        A.add(self, a, b)
        print(a * b)


c = C()
c.add(2, 3)
