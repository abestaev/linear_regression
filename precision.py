import csv
import json

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

if max_km == min_km:
    print("Error: all mileages are identical")
    exit()

m = len(mileages)
mean_price = sum(prices) / m

ss_res = 0
ss_tot = 0
mae = 0 # Mean Absolute Error

for i in range(m):
    mileage_normalized = (mileages[i] - min_km) / (max_km - min_km)
    prediction = theta0 + theta1 * mileage_normalized
    error = prices[i] - prediction
    
    mae += abs(error)
    ss_res += error ** 2
    ss_tot += (prices[i] - mean_price) ** 2

mae = mae / m
mse = ss_res / m

if ss_tot != 0:
    r2 = 1 - (ss_res / ss_tot)
else:
    r2 = 0

print(f"MAE: {mae:.2f}")  # erreur moyenne en valeur absolue
print(f"MSE: {mse:.2f}")  # erreur quadratique moyenne
print(f"R2: {r2:.4f}")    # qualité globale du modèle, proche de 1 = bon


