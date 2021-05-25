print()
print("Hello " * 3)
print("All the power \n is with you")

a, b = 10, 20
print(a, b)
print(a, b, sep=',')
print(a, b, sep='++++')

name = "Bruno"
marks = 93.5678

print("Name is", name, "Marks are", marks)
print("Name is %s, Marks are %f" % (name, marks))
print("Name is %s, Marks are %.2f" % (name, marks))

print("Name is {}, Marks are {}".format(name, marks))
print("Name is {0}, Marks are {1}".format(name, marks))