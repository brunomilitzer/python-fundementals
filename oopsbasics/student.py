class Student:
    major = "CSE"

    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name


s1 = Student(1, "Bruno")
s2 = Student(2, "Tales")
s3 = Student(3, "Vanessa")

print(s1.major)
print(s1.name)

print(s2.major)
print(s2.name)

print(s3.major)
print(s3.name)

print(Student.major)