def printer():
    print("HelloWorld")


def writer():
    print("Hello python")


def display_info(func):
    def inner():
        print("Executing", func.__name__, "function")
        func()
        print("Finished execution")

    return inner


decorated_func = display_info(writer)
decorated_func()
