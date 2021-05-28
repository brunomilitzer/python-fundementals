class Product:

    def __init__(self):
        self.name = "Galaxy S20+"
        self.description = "Galaxy S20+ w/256GB"
        self.price = 1100

    def __del__(self):
        print("Inside the destructor")

    def display(self):
        print("Product Name: ", self.name)
        print("Description: ", self.description)
        print("Price: ", self.price)


p1 = Product()

print(p1.name)
print(p1.description)
print(p1.price)

p2 = Product()
p2.display()
p2 = None
