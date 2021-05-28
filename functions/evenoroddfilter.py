lst = [10, 3, 33, 2, 34, 99]

result = list(filter(lambda x: x % 2 == 0, lst))

print(result)

for i in result: print(i)
