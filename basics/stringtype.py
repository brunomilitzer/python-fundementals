s = "  Hello World   "
print(s)

s1 = """You are a 
very dedicated 
software engineer!"""

print(s1)

print(s[4])
print(s*4)
print(len(s))
print(len(s1))

print(s[0:5])
print(s[0:])
print(s[:5])
print(s[-3:-1])

print(s[0:9:2])
print(s[11::-1])
print(s[::-1])

print(s.strip())
print(s.strip())
print(s.lstrip())
print(s.rstrip())

print(s.find("ld", 0, len(s)))
print(s.find("ld", 0, 8))
print(s.count("l"))
print(s.replace("ell", "ing"))
print(s.upper())
print(s.lower())
print(s.title())