def contact_card(name, age, car_model):
    return f"{name} is {age} and drives a {car_model}"
output = contact_card(name="keith", age= 29, car_model="Honda civic")
print(output)


def can_drive(age, driving_age=16):
    return age >= driving_age
result = can_drive(24, 20)
print(result)