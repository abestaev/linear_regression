import json

theta0 = 0
theta1 = 0

try:
    with open("model.json", "r") as file:
        model = json.load(file)
    if "theta0" in model and "theta1" in model:
        theta0 = model["theta0"]
        theta1 = model["theta1"]

except FileNotFoundError:
    pass

try:
    mileage = float(input("Enter mileage: "))
    price = theta0 + theta1 * mileage
    print(price)

except ValueError:
    print("Invalid mileage")