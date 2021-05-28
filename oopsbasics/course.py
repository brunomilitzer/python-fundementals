class Course:

    def __init__(self, name, ratings):
        self.name = name
        self.ratings = ratings

    def average(self):
        number_of_ratings = len(self.ratings)
        average = sum(self.ratings) / number_of_ratings

        return average


c1 = Course("Java Course", [1, 2, 3, 4, 5])
print(c1.name)
print(c1.average())

for r in c1.ratings:
    print(r)

c2 = Course("Java Web Services", [1, 2, 3, 4, 5])
print(c2.name)
print(c2.average())

for r in c2.ratings:
    print(r)
