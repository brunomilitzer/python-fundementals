lst = [20, 30, 40, 234]
print(type(lst))

b = bytes(lst)

print(type(b))
print(b)
#b[3] = 22

b1 = bytearray(lst)
print(type(b1))
print(b1)
b1[2] = 23

print(b1)