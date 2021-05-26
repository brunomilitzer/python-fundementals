n = int(input("Enter the number of employees: "))
employees = {}

for i in range(n):
    name = input("Enter employee name: ")
    salary = input("Enter employee salary: ")
    employees[name] = salary

while True:
    print("Get employee salary details")
    name = input("Enter employee name: ")
    salary = employees.get(name, -1)
    if salary == -1:
        print("Employee does not exist")
    else:
        print("The salary of hte employee is", salary)

    choice = input("Do you want to know the salary of an other employee[Yes|No]")
    if choice == 'No':
        break
