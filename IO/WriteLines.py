f1 = open("FileFolder/WriteLines", "w+")
seq = ["This 1st line\n", "This 2nd line\n", "This 3rd line\n", "This 4th line\n", "This 5th line\n",
       "This 6th line\n"]
f1.writelines(seq)

print(f1.isatty())  # is associated with a terminal device
f1.seek(0)
print(f1.read())
print(f1.tell())  # Returns the file's current position
