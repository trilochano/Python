data = input("Enter the string : ")

# 1 - Using Slice
revereSlice = data[::-1]
print(revereSlice)

print("---------")
# 2 - Using loops
revereLoop = ""
for i in data:
    revereLoop = i + revereLoop

print(revereLoop)
print("---------")


# 3 - Using Recursion
def reverse(data):
    if len(data) == 0:
        return data
    else:
        return reverse(data[1:]) + data[0]


print(reverse(data))
