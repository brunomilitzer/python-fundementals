class Programmer:

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_salary(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary

    def set_technologies(self, techs):
        self.techs = techs

    def get_technologies(self):
        return self.techs


p1 = Programmer()
p1.set_name("Bruno")
p1.set_salary(4109)
p1.set_technologies(["Java", "SASS", "Python", "JavaScript", "Hibernate", "Spring"])

print(p1.get_name())
print(p1.get_salary())
print(p1.get_technologies())
