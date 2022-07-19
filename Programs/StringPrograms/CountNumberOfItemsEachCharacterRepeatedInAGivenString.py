data = input("Enter the string : ")
# v = set()  # Empty Set
# print(type(v))
eachChars = {}  # Empty Dictionary
# print(type(eachChars))

for i in data:
    if i in eachChars:
        eachChars[i] += 1
    else:
        eachChars[i] = 1

# print(eachChars)
print(str(eachChars))
