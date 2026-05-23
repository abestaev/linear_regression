import json

theta0 = 0
theta1 = 0
min_km = 0
max_km = 0


try:
    with open("model.json", "r") as file:
        model = json.load(file)
    if "theta0" in model and "theta1" in model:
        theta0 = model["theta0"]
        theta1 = model["theta1"]
    if "min_km" in model and "max_km" in model:
        min_km = model["min_km"]
        max_km = model["max_km"]

except FileNotFoundError:
    pass

try:
    mileage = float(input("Enter mileage: "))

    if max_km != min_km:
        mileage = (mileage - min_km) / (max_km - min_km)
        
    price = theta0 + theta1 * mileage
    print(price)

except ValueError:
    print("Invalid mileage")