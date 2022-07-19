f = open("config.txt", 'r+')
n = f.read()
list_of_words = n.split()
reverse_of_words = list_of_words[::-1]
# print(reverse_of_words)

reverese_data = ""

for i in reverse_of_words:
    reverese_data = reverese_data + i +' '

print(reverese_data)
