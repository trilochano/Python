def display_info(func):
    def inner():
        print("Executing", func.__name__, "function")
        func()
        print("Completed Execution")

    return inner


@display_info
def printer():
    print("welcome to my world")


@display_info
def writer():
    print("welcome to python")


writer()
printer()
