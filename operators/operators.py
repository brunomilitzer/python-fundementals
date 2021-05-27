# height = 5.11
# weight = 92

# bmi = weight in kg / (height in meters)

# heightInMeters = height * 0.4536

# bmi = weight / (heightInMeters * heightInMeters)

# print('BMI: ', bmi)


def calculate_bmi(height, weight=70):
    height_in_meters = height * 0.4536

    return weight / (height_in_meters * height_in_meters)


print(calculate_bmi(5.11))
