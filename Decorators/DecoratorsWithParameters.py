def decorator_display(func):
    def inner(a, b):
        print("Dividing", a, 'by', b)
        if b == 0:
            print("Can't divide")
            return
        return func(a, b)

    return inner


@decorator_display
def divide(a, b):
    return a / b


value1 = divide(10, 2)
print(value1)

value2 = divide(10, 0)
print(value2)
