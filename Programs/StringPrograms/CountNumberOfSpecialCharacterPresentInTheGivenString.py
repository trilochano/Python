data = input("Enter the string : ")
alphabets = digits = special = 0

# 1 Using Predefine methods
# for i in range(len(data)):
#     if data[i].isalpha():
#         alphabets = alphabets + 1
#     elif data[i].isdigit():
#         digits = digits + 1
#     else:
#         special = special + 1
#
# print("Alphabets : ", alphabets)
# print("Digits : ", digits)
# print("Special  : ", special)

# 2 Without using Predefine methods
print("--------------------------------------------------------------------")
for i in range(len(data)):
    if ('a' <= data[i] <= 'z') or ('A' <= data[i] <= 'Z'):
        pass
        alphabets = alphabets + 1
    elif '0' <= data[i] <= '9':
        pass
        digits = digits + 1

    else:
        special = special + 1

print("Alphabets : ", alphabets)
print("Digits : ", digits)
print("Special  : ", special)
