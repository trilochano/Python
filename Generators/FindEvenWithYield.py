def even_generator():
    n1 = 0

    n1 += 2
    yield n1

    n1 += 2
    yield n1

    n1 += 2
    yield n1


numbers = even_generator()
print(next(numbers))
print(next(numbers))
print(next(numbers))

