data = input("Enter elements of a list")
OriginalList = data.split()

WithOutDuplicates=[]
onlyDuplicates=[]

for i in OriginalList:
    if i not in WithOutDuplicates:
        WithOutDuplicates.append(i)
    else:
        onlyDuplicates.append(i)


print("Original List           :",OriginalList)

print("Only Duplicates List    :",onlyDuplicates)

print("WithOut Duplicates List :",WithOutDuplicates)




