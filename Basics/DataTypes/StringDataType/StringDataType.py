name = 'Trilochan'
fullName = "TrilochanaReddy"
lastName = "'Trilochan'ObulaReddy"
sentence = "'Hi this is trilochan" \
        " trilochan is good boy'"

para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print(para_str)

print(name)
print(fullName)
print(lastName)
print(sentence)


# Accessing Values in Strings
print("------Accessing Values in Strings-------")
print(name[0])
print(name[-1])
print(name[1:])
print(name[:5])
print(name[:8:])
print(name[1:5])

print("--------------------------------")

# Updating Strings
print(fullName[:16]+' Obulareddy')

#String Special Operators
print('T' in fullName )
print('w' not in fullName)
print(fullName*2)


#String Formatting Operator
print("My name is %s and weight is %d kg!" % ('Trilochan', 60))
print("My name startts with %c" % ('T'))