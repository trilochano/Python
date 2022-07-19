f1 = open("triWriteFile.xt", "a")
print("Name of the file   ", f1.name)
print("closed r not  ", f1.closed)
print("Mode", f1.mode)
f1.write("  Python")

print("---------------------------------------------------------")

f1 = open("triWritePlusFile.txt", mode="a+")
print("Name of the file   ", f1.name)
print("closed r not  ", f1.closed)
print("Mode", f1.mode)
f1.write(" Welcome, Python World")
print(f1.tell())
f1.seek(0)
readAFile = f1.read()
print(readAFile)

