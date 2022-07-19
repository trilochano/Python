def generate_fibonacci():
    n1 = 0
    yield n1

    n2 = 1
    yield n2

    while True:
        n1, n2 = n2, n1 + n2
        yield n2


seq = generate_fibonacci()
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))



