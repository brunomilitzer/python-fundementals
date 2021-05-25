id = 1
firstName = "Tom"
lastName = "    Bailey"
ssn = "123-45-6789"
hasInsurance = True
billingAmount = "1000"
print(type(billingAmount))
billingAmount = float(billingAmount)
print(type(billingAmount))

print(id, firstName, lastName.lstrip(), ssn, hasInsurance, ssn[7:len(ssn)])