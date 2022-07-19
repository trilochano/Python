class Dog:
    """Common Class"""
    # class attribute
    attr1 = "mammal"

    # Instance attribute
    def __init__(self, name):
        self.name = name


# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")
print("--------------------------------")
# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))
print("--------------------------------")
# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))


print("--------------------------------")
# Built-In Class Attributes
print(Dog.__class__)
print(Dog.__doc__)
print(Dog.__module__)
print(Dog.__bases__)
print(Dog.__dict__)
print(Dog.__name__)
print(Dog.__base__)
