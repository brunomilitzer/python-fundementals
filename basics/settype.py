s = {10, 20, 30, 'xyz', 10, 20}
print(s)
print(type(s))

s.update([33, 11])

print(s)
print(type(s))

#print(s[0:5])
#print(s*3)

s.remove(33)
print(s)

f = frozenset(s)
print(f)
print(type(f))