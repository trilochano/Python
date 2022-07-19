import re

# name = 'Trilochana'
# regex = '[a,e,i,o,u]'

# for i,v in enumerate(name):
#     if re.match(regex, v):
#         print(i, v)


# vowels = ['a', 'e', 'i', 'o', 'u']
# for i,v in enumerate(name):
#     if v in vowels:
#         print(i,v)

regex_for_ip = '((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'

ip = input("enter the ip address")

if re.match(regex_for_ip, ip):
    print("Valid Ip address")
else:
    print("Invalid Ip address")
