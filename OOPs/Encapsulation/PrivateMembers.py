# Python program to
# demonstrate private members

# Creating a Base class


class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks2"


# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)


# Driver code
obj1 = Base()
print(obj1.a)

# print(obj1.c)
# Uncommenting  will
# raise an AttributeError


obj2 = Derived()
# Uncommenting  will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class
