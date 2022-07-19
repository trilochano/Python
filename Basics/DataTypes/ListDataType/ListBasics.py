list1 = [10, 20, 30, 40, 50]
t1 = [1, 2, 3, 4, 5]
list2 = ['Trilochan', 'Reddy', 'QA']
list3 = [121, 'Trilochana', 54153.90]

print("----Access List-------")
print("list1[1:4]  :",t1[1:5])
print("list3[1:]   :",list3[1:])
print("list3[1:]   :",list3[:1])
print("list1[1:4]  :",list1[1:4])
print("list2[:-1]  :",list2[:-1])

print("----Update List-------")

# Update List
print(list2[2])
print(list2)
list2[2]='Automation'
print(list2[2])
print(list2)

print("----Delete List-------")

#Delete List
print(list2)
del list2[2]
print(list2)

print("----Baisc List Operators-------")
#Basic List Operators
print(len(list1))
print(list1+[4,5,6])
print(list1*2)
print(10 in list1)
print(10 not in list1)
for i in list1:
    print(i)


