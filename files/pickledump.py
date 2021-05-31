import pickle, student

f = open("student.dat", "wb")
s = student.Student(123, "Bruno", 92)
pickle.dump(s, f)
f.close()

