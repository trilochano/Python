from abc import ABC, abstractmethod


class Polygon(ABC):
    def __init__(self):
        print("Abstract Class")

    @abstractmethod
    def noofsides(self):
        print("Polygon")
        pass


class Triangle(Polygon):
    def noofsides(self):
        Polygon.noofsides(self)
        print("I Have 3 sides")


class Square(Polygon):
    def noofsides(self):
        Triangle.noofsides(self)
        print("I Have 4 sides")


# p=Polygon() # TypeError: Can't instantiate abstract class Polygon with abstract methods noofsides
s = Square()
s.noofsides()
