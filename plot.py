import csv
import json
import matplotlib.pyplot as plt

mileages = []
prices = []

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        mileages.append(float(row["km"]))
        prices.append(float(row["price"]))
    
with open("model.json", "r") as file:
    model = json.load(file)

theta0 = model["theta0"]
theta1 = model["theta1"]
min_km = model["min_km"]
max_km = model["max_km"]

x_values = [min(mileages), max(mileages)]
y_values = []

for mileage in x_values:
    mileage_normalized = (mileage - min_km) / (max_km - min_km)
    predicted_price = theta0 + theta1 * mileage_normalized
    y_values.append(predicted_price)

plt.scatter(mileages, prices)
plt.plot(x_values, y_values)

plt.xlabel("Mileage")
plt.ylabel("Price")
plt.title("Linear regression")
plt.show()

