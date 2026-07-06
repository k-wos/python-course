from functools import reduce

sum = lambda a,b: a + b

print(sum(1,2))

def generateLambda(num):
    return lambda a: a * num

doubler = generateLambda(2)
print(doubler(4))
print(doubler(5))

listData = [0,1,2,3]

result = list(map(lambda a: a * 3, listData))
print(result)

result = list(filter(lambda a: a < 2, listData) )
print(result)

result = reduce(lambda x,y: x + y, ("Ola", "Ania", "Tomek"))
print(result)