# complex can't convert into int ,float
a = 10
b = 20.5
c = 4 + 7j

a1, b1, c1 = 100, 200, 300
# del a1
print(a1, b1, c1)


print(type(a))
print(type(b))
print(type(c))
#
print(" ")
print("Int Conversions :")
d = int(a)
print(type(d))
print(d)
#
# # e = int(c)
# # print(type)
# # print(e)
#
# print(" ")
# print("Float Conversions :")
#
# g = float(a)
# print(type(g))
# print(g)
#
# # h = float(c)
# # print(type(h))
# # print(h)
#
print(" ")
print("Complex Conversions :")
i = complex(a)
print(type(i))
print(i)

j = complex(b)
print(type(j))
print(j)
