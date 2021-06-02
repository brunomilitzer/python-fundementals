from numpy import *

arr = array([1, 2, 3, 4, 5], int)
carr = array(['a', 'b', 'c'], dtype=str)
sarr = array(['Python', 'Java', 'Angular'])

print(arr)
print(carr)
print(sarr)

print(linspace(0, 100, 20))
larr = logspace(1, 20)

"""
for i in larr:
    print(i)
"""

print(arange(100, 1, -2))
print(arange(1, 100))

print(zeros(20))
print(ones(20))