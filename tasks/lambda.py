from functools import reduce

names = ["Ola", "Ania", "Kasia"]

fullName = list(map(lambda a: a + " Kowalska", names))
print(fullName)

filtered = list(filter(lambda a: len(a) > 12, fullName))
print(filtered)

numbers = [1,2,3,4,5]

totalSum = reduce(lambda a,b: a + b, numbers)

average = totalSum / len(numbers)

print(average)

users = [
    {'name': 'Jan', 'age': 11},
    {'name': 'Anna', 'age': 30},
    {'name': 'Piotr', 'age': 40},
    {'name': 'Helena', 'age': 21}
]

filtered = list(filter(lambda a: a['age'] > 18, users))

doubledAge = list(map(lambda a: a['age'] * 2, filtered))

sumAge = reduce(lambda a,b: a+b, doubledAge)
print(sumAge)
