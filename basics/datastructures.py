students = {'bob': ['Python', 'Java', 'DRF'], 'john': ['Spring Data', 'Docker'], 'jim': ['Javascript', 'Angular']}

keys = students.keys()

for eachKey in keys:
    print("\nCourses taken by ", eachKey, " are: ")

    for eachCourse in students[eachKey]:
        print(eachCourse)