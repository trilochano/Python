def star(func):
    def inner(arg):
        print("*" * 20)
        func(arg)
        print("*" * 20)

    return inner


def percent(func):
    def inner(arg):
        print("%" * 20)
        func(arg)
        print("%" * 20)

    return inner

@star
@percent
def display(message):
    print(message)


display("Welcome to python")







