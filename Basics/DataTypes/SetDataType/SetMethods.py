s1 = {1, 4, 5, 6, 8, 9, 90, 87, 0}
s2={1000,2000}
# s1.remove(2)
# print(s1)
s1.discard(2)
print(s1)
s1.update({99, 100})
s1.update(s2)
print(s1)
