numbers = [7,8,9,10,11,12]
print(numbers)

tupleNumbers = tuple(numbers)

print(type(tupleNumbers))
print(tupleNumbers)

mixedList = [1.21, 231, "Rower", 21]
print(mixedList)

setMixed = set(mixedList)
print(type(setMixed))
print(setMixed)

frozenSetNumbers = frozenset(tupleNumbers)
print(type(frozenSetNumbers))
print(frozenSetNumbers)

nameAgePairs = (("Natalia", 23), ("Przemek", 30), ("Marek", 21))
ageDict = dict(nameAgePairs)

print(ageDict)
print(ageDict["Marek"])