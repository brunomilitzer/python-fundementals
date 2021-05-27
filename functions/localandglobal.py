x = 123


def display():
    y = 678
    x = 777
    print(x)
    print(y)
    print(globals()['x'])


print(x)
# print(y)
# display()
z = display

z()
z()
z()
