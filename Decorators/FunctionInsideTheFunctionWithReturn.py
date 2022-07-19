# Inner function is a closer
def print_msg(message):
    greeting = 'Welcome'

    def printer():
        print(greeting, message)

    return printer


func = print_msg("To Python")
func()
