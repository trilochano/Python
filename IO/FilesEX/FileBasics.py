# r: open an existing file for a read operation.
# w: open an existing file for a write operation. If the file already contains some data then it will be overridden.
# a:  open an existing file for append operation. It won’t override existing data.
#  r+:  To read and write data into the file. The previous data in the file will not be deleted.
# w+: To write and read data. It will override existing data.
# a+: To append and read data from the file. It won’t override existing data.


# f = open("config.txt")
# print(f.mode)
# print(f)
# print(f.close())
# print(f.read())
# print(f.closed)


# r
# <_io.TextIOWrapper name='config.txt' mode='r' encoding='cp1252'>c
# None
# True


# Read:
# f = open("config.txt", 'r')
# print(f.read())
# f.seek(3)
# print(f.read())
# print(f.tell())

# write
# f = open("config.txt", 'w')
# f.write("12\n3")


# r+
# f = open("config.txt", 'r+')
# f.write("123456")
# print(f.read())


# w+

f = open("config.txt", 'w+')
f.write("123456")
f.seek(0)
print(f.read())

# a
# f = open("config.txt", 'a')
# f.write("welcome")
# f.seek(0)
# print(f.read())

# a+
# f = open("config.txt", 'a+')
# f.write(" HI")
# f.seek(0)
# print(f.read())
