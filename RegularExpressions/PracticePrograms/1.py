import re

# Write a Python program to check that a string contains only a certain set
# of characters (in this case a-z, A-Z and 0-9).


sentence = input("Enter the string  : ")


def checking(sentence):
    verify = re.search("[^A-Za-z0-9]", sentence)
    return not bool(verify)


print(checking(sentence))
