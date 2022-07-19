# def division(a, b):
#     try:
#         c = ((a + b) / (a - b))
#     except ZeroDivisionError:
#         print("a/b result in 0")
#     else:
#         print("C Value = ", c)
#
#
# division(2, 3)
# division(3, 3)

def tryWithElse():
    try:
        print("Try Block")
        # c = 2 / 0
        # print(c)
    except ZeroDivisionError:
        print("Except Block")
    else:
        print("Else Block")


tryWithElse()

print("--------------------------------------------------")


def tryWithElseWithFinally():
    try:
        print("Try Block")
        c = 2 / 0
        print(c)
    except ZeroDivisionError:
        print("Except Block")
    else:
        print("Else Block")
    finally:
        print("Finally Block")


tryWithElseWithFinally()
