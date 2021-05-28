class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.clinical = []

    def add_clinical_data(self, clinical):
        self.clinical.append(clinical)


class Clinical:
    def __init__(self, component_name, component_value):
        self.component_name = component_name
        self.component_value = component_value


p = Patient("Vanessa", 41)
c1 = Clinical("HR", 62)
c2 = Clinical("BP", "80/120")
p.add_clinical_data(c1)
p.add_clinical_data(c2)

print(p.name)

for each_clinical in p.clinical:
    print(each_clinical.component_name)
    print(each_clinical.component_value)

