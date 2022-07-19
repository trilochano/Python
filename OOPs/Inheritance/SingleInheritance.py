# class A:
#     age = '20'
#
#     def getName(self, name):
#         return name
#
#
# class B(A):
#     pass
#
# b=B()
# print(b.getName('trilochan'))
# print(b.age)



# class A:
#     age = '20'
#
#     def getName(self, name):
#         print("A")
#         return name
#
#
# class B(A):
#     pass
#     # def getName(self, name):
#     #     print("B")
#     #     return name
#
# b=B()
# print(b.getName('trilochan'))
# print(b.age)




# class A:
#     # age = '20'
#
#     def getName(self, name):
#         print("A")
#         return name
#
#
# class B(A):
#     age = '20'
#     def getName(self, name):
#         print("B")
#         return name
#
# a=A()
# print(a.getName('trilochan'))
# print(a.age)




# class Student:
#     count = 0
#     def __init__(self):
#         Student.count = Student.count + 1
#         print(Student.count)
# s1=Student()
# s2=Student()
# s3=Student()
# print("The number of students:",Student.count)


class Student:
    def __init__(self):
        print("The First Constructor")

    def __init__(self):
        print("The second contructor")

    def __init__(self):
        print("The third contructor")




st = Student()






