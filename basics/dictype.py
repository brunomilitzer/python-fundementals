dict1 = {1: 'tom', 2: 'bob', 3: 'bill'}
print(dict1)
print(type(dict1))

print(dict1.items())
print(dict1.keys())
print(dict1.values())

k = dict1.keys()

for i in k: print(i)

v = dict1.values()

for i in v: print(i)

print(dict1[3])

del dict1[1]

print(dict1)

