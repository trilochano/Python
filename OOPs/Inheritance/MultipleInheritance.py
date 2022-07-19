# class A:
#     pass
#     # def __init__(self):
#     #     print("C")
#
#
# class B:
#     def __init__(self):
#         print("B")
#
#
# class C(A, B):
#     pass
#     # def __init__(self):
#     #     print("C")
#
#
# c = C()


class School:
    school_name = "high school"

    def __init__(self, class_name):
        self.class_name = class_name

    def schoolname(self):
        print("This method is called from School Class    : ,",self.school_name)


class College:
    college_name = "College"

    def __init__(self, degree):
        self.degree = degree

    def collegename(self):
        print("This method is called from College Class   : ,",self.college_name)


class Student(School, College):
    student_name = "Trilochan"

    def __init__(self, address):
        self.address = address


stud = Student("Andhra Pradesh")
stud.schoolname()
stud.collegename()
