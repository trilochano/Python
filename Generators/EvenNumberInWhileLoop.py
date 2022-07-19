def even_generators(max):
    n = 2
    while n <= max:
        yield n
        n += 2


num = even_generators(10)

for i in num:
    print(i)
