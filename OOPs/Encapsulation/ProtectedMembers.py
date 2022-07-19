# Python program to
# demonstrate protected members

# Creating a base class
class Base:
    def __init__(self):
        # Protected member
        self.a = 2
        print(self.a)


# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling protected member of base class: ",
              self.a)

        # Modify the protected variable:
        self.a = 3
        print("Calling modified protected member outside class: ",
              self.a)


obj1 = Derived()

obj2 = Base()

# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", obj1.a)

# Accessing the protected variable outside
print("Accessing protected member of obj2: ", obj2.a)
