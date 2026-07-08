import math, random

print(type(str(12)))

print(math.ceil(11.000000001))
print(math.floor(11.000000001))

print(round(12.3215123, 2))

print(random.random())
print(random.random()*100)
print(int(random.random()*100))

print(random.choice([1,3,523,31,31,314]))

print(random.randrange(-10,30, 5))

listDAta = [0,1,2,3,4,5,6,7]
random.shuffle(listDAta)

print(listDAta)