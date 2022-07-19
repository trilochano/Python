# Syntax raise [Exception [, args [, traceback]]]
# try:
#     raise NameError("Hi there")  # Raise Error
# except NameError:
#     raise  # To determine whether the exception was raised or not

try:
    raise ArithmeticError("Divide by zero")  # Raise Error
except ArithmeticError:
    raise  # To determine whether the exception was raised or not


