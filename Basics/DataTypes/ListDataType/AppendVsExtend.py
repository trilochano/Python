list1 = [10, 20, 30, 40, 50,40,50,20]
list2 = ['Trilochan', 'Reddy', 'QA']

list1.append(list2)
print(list1) # [10, 20, 30, 40, 50, 40, 50, 20, ['Trilochan', 'Reddy', 'QA']]

list1.extend(list2)
print(list1) # [10, 20, 30, 40, 50, 40, 50, 20, 'Trilochan', 'Reddy', 'QA']

list1.append(2)
print(list1) # [10, 20, 30, 40, 50, 40, 50, 20, 2]

list1.extend(2)
print(list1) # TypeError: 'int' object is not iterable

list1.append([2])
print(list1) # [10, 20, 30, 40, 50, 40, 50, 20, [2]]

list1.extend([2])
print(list1) # [10, 20, 30, 40, 50, 40, 50, 20, 2]








