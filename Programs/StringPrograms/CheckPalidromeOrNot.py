data = input("Enter the string : ")
print("--------------------------")

# 1 - Using Slice
# revere = data[::-1]

# if data == revere:
#     print("Palindrome String :" + revere)
# else:
#     print("Not Palindrome")

print("--------------------------------------")

# # 2 - Using loops
# revere = ""
# for i in data:
#     revere = i + revere
#
# if data == revere:
#     print("Palindrome String :" + revere)
# else:
#     print("Not Palindrome")

print("--------------------------------------")


# 3 - Using Recursion
def reverse(data):
    if len(data) < 1:
        return True
    else:
        if data[0] == data[-1]:
            return reverse(data[1:-1])
        else:
            return False

if(reverse(data) == True):
    print("Palindrome String :" , data)
else:
    print("Not Palidrome")



print("--------------------------")

# 4 - with out using slice
# def iterative(data):
#     for i in range(0,int(len(data)/2)):
#         if data[i] != data[len(data)-i-1]:
#             return False
#     return True
#
# reverse1=(iterative(data))
# if(reverse1):
#     print("Palindrome String :" ,data)
# else:
#     print("Not Palidrome")



