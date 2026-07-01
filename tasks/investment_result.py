capital = 5000
rateOfInterest = 0.08
inflationRate = 0.15

earnedMoney = capital * rateOfInterest
print(earnedMoney)

lostMonet = capital * inflationRate
print(lostMonet)

newCapital = capital + earnedMoney - lostMonet
print(newCapital)