f1 = open("triWritePlusFile.txt", "r+")
print(f1.isatty())  # is associated with a terminal device
f1.seek(0)
print(f1.read())
print(f1.tell())  # Returns the file's current position
count = f1.truncate()
print(count)