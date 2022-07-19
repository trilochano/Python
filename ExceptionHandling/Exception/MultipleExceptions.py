try:
    name = 'Bob'
    name += 1

except (NameError, TypeError) as error:
    print(error.args)
else:
    print(name)
