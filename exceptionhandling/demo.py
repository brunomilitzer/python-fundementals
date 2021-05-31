import logging

logging.basicConfig(filename="mylog.log", level=logging.DEBUG)

try:
    f = open("myfile.txt", "w")
    a, b = [int(x) for x in input("Please enter two numbers: ").split()]
    logging.info("Division in progress")
    c = a / b
    f.write("Writing %d into file" % c)
except ZeroDivisionError:
    print("Division by zero is not allowed")
    print("Please a non zero number")
    logging.error("Division by zero is not allowed")
else:
    print("You have entered a non zero number")
finally:
    f.close()
    print("File closed")

print("Code after the exception")
