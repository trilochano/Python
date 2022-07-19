spaces2 = '88888welcome to my world88888'
txt = "Thank you for the music\nWelcome to the jungle\nWelcome to the world"

print(spaces2.split(" "))
print(spaces2.split(" ", 2))

print(txt)
print(txt.splitlines())
print(txt.splitlines(True))
print(txt.splitlines(False))

print(spaces2.zfill(50))
print(spaces2.rjust(50, '0'))
print(spaces2.ljust(50, '0'))
