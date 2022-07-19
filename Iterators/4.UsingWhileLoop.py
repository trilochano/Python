l1 = [1, 2, 3, 7]
values = iter(l1)

while (True):
    try:
        element = next(values)
        print(element)
    except StopIteration:
        break


