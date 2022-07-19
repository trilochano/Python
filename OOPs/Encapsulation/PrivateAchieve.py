class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks2"

    def __privateMethod(self):
        print("Private Method")

    def access_private_members(self):
        print(self.__c)
        self.__privateMethod()

    def _protectedMethod(self):
        print("Protected")


b = Base()
print(b.a)
b.access_private_members()
b._protectedMethod()



