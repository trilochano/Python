f1 = open("triWritePlusFile.txt", "r+")
print("Name of the file   ", f1.name)
print("closed r not  ", f1.closed)
print("Mode", f1.mode)
print(f1.readline(30))
# print(f1.readline())
# print(f1.readline())
print("---------------------------------------------------------")
print(f1.readlines())

