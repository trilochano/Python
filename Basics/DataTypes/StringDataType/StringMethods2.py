name = 'trilochan'
fullName = "Trilochana reddy"
lastName = "'Trilochan'ObulaReddy"
spaces1 = ' welcome to my world '
spaces2 = '88888welcome to my world88888'
isAlpha = '1234\tqqqqqqqqqqqqqq1234'
number = 123
seq=('a','b','c')
str = "this is string example....wow!!!"

print(fullName.count('a', 3, len(fullName)))
print(spaces2.endswith("88888",0,len(spaces2)))
print(spaces2.endswith("88888",0,5))
print(spaces2.startswith("88888",0,5))


print(isAlpha.expandtabs())
print(isAlpha.expandtabs(16))
print(isAlpha.expandtabs(24))

print(lastName.find('a',15,len(lastName)))
print(lastName.index('a',15,len(lastName)))

s='-'
print(s.join(seq))

print(name.ljust(13,'-'))
print(name.rjust(13,'='))


print(str.replace('is','was'))
print(str.replace('is','was',2))

print(str.index('is'))
print(str.rindex('is'))
print(str.find('is'))
print(str.rfind('is'))
print(str.rfind('is',0,10))
print(str.find('is',0,10))




