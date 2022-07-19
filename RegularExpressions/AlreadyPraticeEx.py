#1.[]:	A set of characters:
#Find all [a z],[A Z],[0 9],[ABC],[abc],[^abc] characters:
import re
#
family="i have a family with 10 members.All are working in the fields."
x=re.findall("[a-z]",family,flags=re.IGNORECASE)
print(x)
# family="i have a family with 10 members.all are working in the fields."
# x=re.findall("[A-Z]",family)
# print(x)
# family="i have a family with 10 members.All are working in the fields."
# x=re.findall("[0-9]",family)
# print(x)
# family="i have a family with 10 members.all are working in the fields."
# x=re.findall("[abc]",family)
# print(x)
# family="i have a family with 10 members.All are working in the fields."
# x=re.findall("[ABC]",family)
# print(x)
# family="i have a family with 10 members.All are working in the fields."
# x=re.findall("[^abc]",family)
# print(x)
# family="i have a family with 10 members.All are working in the fields."
# x=re.findall("[^ABC]",family)
# print(x)
#
# #2.\:Signals a special sequence (can also be used to escape special characters):
# #Find all digit characters:
# money="i have 25rs.For that i will buy 5rs chocolates 5 qty.And 3rs chocolates 8qty. 123456789"
# m=re.findall("\d+",money)
# print(m)

# #3) .   :Any character (except newline character)
# #Search for a sequence that starts with "ch", followed by two (any) characters, and an "s":
# buy="i have 25rs.For that i will buy 5rs chocolates 5 qty.And 3rs chocolates 8qty."
# x=re.findall("cho......s",buy)
# print(x)
# ANS::['chocolates', 'chocolates']

# 4.^ ::Starts with
# it will Check if the string starts with 'hello':
# family="hello,i have a family with 10 members.all are working in the fields."
# x=re.findall("^hello",family)
# if x:
#     print("yes hello  present in family")
# else:
#     print("no")---------------------------------           #ans:YES HELLO PRESENT IN FAMILY
#
# family="hello,i have a family with 10 members.all are working in the fields."
# x=re.findall("^have",family)
# if x:
#     print("yes have  present in family")
# else:
#     print("no")---------------------------------#ANS: NO

# 5.ENDS WITH($):
# family="hello,i have a family with 10 members.all are working in the fields."
# x=re.findall("have$",family)
# if x:
#     print("yes have ENDS in family")
# else:
#     print("no")
#
# family="hello,i have a family with 10 members.all are working in the fields."
# x=re.findall("fields.$",family)
# if x:
#     print("yes fields ends in family")
# else:
#     print("no")

# 6.Zero or more occurrences(*)::
# buy="i have 25rs.For that i will buy 5rs chocolates 5 qty.And 3rs chocolates 8qty."
# x=re.findall("h.*e",buy)
# print(x)
# # 7.One or more occurrences(+)::
# buy = "i hello 25rs.For that i will buy 5rs chocolates 5 qty.And 3rs chocolates 8qty."
# x = re.findall("h.+e", buy)
# print(x)
# buy = "hae"
# x = re.findall("h.+e", buy)
# print(x)
#
# # 8.# 6.Zero or One occurrences(?)::
# buy = "i have 25rs.foooor that i will buy 5rs chocolates 5 qty.And 3rs chocolates 8qty."
# x = re.findall("f.?r", buy)
# print(x)
# # #9.	Exactly the specified number of occurrences{2}::
# buy = "hello,i have 25rs.For that i will buy 5rs chocolates 5 qty.And 3rs chocolates 8qty."
# x = re.findall("he{2,9}", buy)
# print(x)
#
# import re
#
# # 1.
# d = "trilochana rteddy obulreddy"
# x = re.findall("a", d)
# print(x)
# # 2.
# x = re.search("\s", d)
# print(x.start())
#
# # 3.
# x = re.split("\s", d, 2)
# print(x)
#
# # 4.
# x = re.sub("\S", "space", d, 2)
# print(x)
#
# # 5.
x = re.search("tri", d)
print(x)

# Ex = "The rain in spain"
# d = re.findall("\AThe", Ex)
# print(d)
# d1 = re.findall("\bpain", Ex)
# print(d1)
