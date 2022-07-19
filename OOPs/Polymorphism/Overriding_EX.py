class Animal:
    def move(self):
        print("Animal Move")

    def eat(self):
        print("Animal eat")


class dog(Animal):
    def move(self):
        super().move()
        Animal.move(self)
        print("4 Legs")

    def eat(self):
        super().eat()
        Animal.eat(self)
        print("Bis")


a = dog()
a.move()
a.eat()
