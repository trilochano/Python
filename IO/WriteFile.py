# Syntax: file object = open(file_name [, access_mode][, buffering])
# Default access_mode is r(Not given)
# W means only writing
# W+ means Write and Read ,Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
# r+ means Write and Read.The file pointer placed at the beginning of the file.
# a Opens a file for appending.
# a+ Opens a file for both appending and reading



f1 = open("triWriteFile.xt","w")
print("Name of the file   ", f1.name)
print("closed r not  ", f1.closed)
print("Mode", f1.mode)
f1.write("TrilochanReddy")

print("---------------------------------------------------------")

f1 = open("triWritePlusFile.txt","w+")
print("Name of the file   ", f1.name)
print("closed r not  ", f1.closed)
print("Mode", f1.mode)
f1.write("TrilochanReddy")
f1.seek(0)
readAFile=f1.read()
print(readAFile)

