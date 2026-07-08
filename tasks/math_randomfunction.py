import math, random
distance = random.randint(100,1000)

fuelConsuption = math.ceil(distance / 100) * 7

fuelPrice = round(random.uniform(4.5, 5.5), 2)

totalCost = round(fuelConsuption * fuelPrice, 2)
print("Koszt: ", totalCost)