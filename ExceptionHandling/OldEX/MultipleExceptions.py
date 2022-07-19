
# try:
#     a = 10 / 8;
#     f = open("Files/Exceptions", 'r')
#     f.write("This is trilochan")
# except(ArithmeticError, IOError) as e:
#     print(e.args)

print("-------------------------------------------")

def fun(a):
    if  a<4:
        b=a-a/(a-3)
        print("Value of b = ",b)


try:
    fun(6)
    fun(5)
except ZeroDivisionError as e:
    print(e.args)
except NameError as e:
    print(e.args)
