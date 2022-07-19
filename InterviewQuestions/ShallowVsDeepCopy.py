import copy

# l1 = [1, 2, 3, 4]
# l2 = []
# l2 = l1
# print(l1, l2)
#
# l2[2] = 500
#
# print(l1, l2)  # Becoz same memory(=)
#
# print(id(l1))
# print(id(l2))

# # Shallow Copy
# print("-------------------------------------")
# l3 = [1, 2, 3, 4]
# l4 = []
# l4 = l3.copy()
#
# print(l3, l4)
# print(id(l3))
# print(id(l4))
#
# l4[2] = 500
# print(l3, l4)

# Shallow Copy by nested List
print("-------------------------------------")
#
# l5 = [[1, 2, 3, 4], [5, 6, 7, 8]]
# l6 = []
# l6 = l5.copy()
# print(l5, l6)
# print(id(l5))
# print(id(l6))
#
# l5[1][0] = 500
# print(l5, l6)
#
# l5.append([9, 10])
# print(l5, l6)

# # Deep Copy with normal list
# print("-------------------------------------")
# l7 = [1, 2, 3, 4]
# l8 = []
# l8 = copy.deepcopy(l7)
# print(l7, l8)
# print(id(l7))
# print(id(l8))
#
# l7[1] = 500
# print(l7, l8)
#
# Deep Copy with nested list
print("-------------------------------------")

l9 = [[1, 2, 3, 4], [7, 8, 9, 10]]
l10 = []
l10 = copy.deepcopy(l9)

l10[1][0] = 500
print(l9, l10)
print(id(l9))
print(id(l10))
