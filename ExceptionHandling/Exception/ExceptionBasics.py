# Exceptions: Exceptions are raised when the program is syntactically correct,
# but the code resulted in an error. This error does not stop the execution of the program,
# however, it changes the normal flow of the program.

try:
    with open("t.txt", 'r') as f:
        f.read()
except IOError:
    print("File Not Found")
else:
    print("Else Block")
finally:
    print("Finally Block")

    



