def print_msg(message):
    gretting = 'Hello'

    def printer():
        print(gretting, message)

    printer()

print_msg("Python is awesome")
