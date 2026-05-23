import csv

mileages = []
prices = []

try:
    with open("data.csv", "r") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames is None:
            print("Error: empty dataset")
            exit()

        if "km" not in reader.fieldnames or "price" not in reader.fieldnames:
            print("Error: missing columns")
            exit()

        for line_number, row in enumerate(reader, start = 2):
            if None in row or row["km"] is None or row["price"] is None:
                print(f"Error: invalid line at line {line_number}")
                exit()

            try:
                mileage = float(row["km"])
                price = float(row["price"])
            
            except ValueError:
                print(f"Error: non numeric value at line {line_number}")
                exit()
            
            mileages.append(mileage)
            prices.append(price)

except FileNotFoundError:
    print("Error: data.csv not found")
    exit()

if len(mileages) == 0:
    print("Error: empty dataset")
    exit()

theta0 = 0
theta1 = 0
learning_rate = 1
iterations = 1000
m = len(mileages)

min_km = min(mileages)
max_km = max(mileages)

normalized_mileages = []

for mileage in mileages:
    km_normalized = (mileage - min_km) / (max_km - min_km)
    normalized_mileages.append(km_normalized)


for i in range(iterations):
    sum_theta0 = 0
    sum_theta1 = 0

    for j in range(m):
        prediction = theta0 + theta1 * normalized_mileages[j]
        error = prediction - prices[j]

        sum_theta0 += error
        sum_theta1 += error * normalized_mileages[j]
    
    tmp_theta0 = learning_rate * (1 / m) * sum_theta0
    tmp_theta1 = learning_rate * (1 / m) * sum_theta1

    theta0 = theta0 - tmp_theta0
    theta1 = theta1 - tmp_theta1


print(theta0)
print(theta1)

import json

model = {
    "theta0": theta0,
    "theta1": theta1,
    "min_km": min_km,
    "max_km": max_km
}

with open("model.json", "w") as file:
    json.dump(model, file, indent=4)
