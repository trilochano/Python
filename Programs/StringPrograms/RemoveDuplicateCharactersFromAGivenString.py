data = input("Enter the string : ")

withOutduplicates = ""

for i in data:
    if i not in withOutduplicates:
        withOutduplicates += i

print(withOutduplicates)