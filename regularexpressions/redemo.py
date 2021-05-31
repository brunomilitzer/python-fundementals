import re

str = "Take 1 up 1-6-2021 One 23 idea. One 45 idea at a time 12-11-2021"
result = re.search(r'o\w\w', str)
# print(result.group())

result2 = re.findall(r'o\w\w', str)
print(result2)

result3 = re.match(r'T\w\w', str)
print(result3.group())

result4 = re.split(r'\d+', str)
print(result4)

result5 = re.sub(r'\d+', '', str)
print(result5)

result6 = re.findall(r'O\w+', str)
print(result6)

result7 = re.findall(r'O\w?', str)
print(result7)

result8 = re.findall(r'O\w{1,2}', str)
print(result8)

result9 = re.findall(r'\d{1,2}-\d{1,2}-\d{4}', str)
print(result9)

result10 = re.search(r'^T\w*', str)
print(result10.group())