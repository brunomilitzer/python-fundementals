"""
class Student:
    def __init__(self):
        self.__id = 123
        self.__name = "Tales"

    def display(self):
        print(self.__id)
        print(self.__name)


s = Student()
s.display()
# print(s._Student__id) wrong way
# print(s._Student__name) wrong way

"""

class Student:
    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


s = Student()
s.set_id(123)
s.set_name("Vanessa")

print(s.get_id())
print(s.get_name())