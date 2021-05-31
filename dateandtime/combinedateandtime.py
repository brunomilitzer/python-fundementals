from datetime import *

d = date(2021, 6, 1)
t = time(16, 34, 11)

dt = datetime.combine(d, t)

print(dt)