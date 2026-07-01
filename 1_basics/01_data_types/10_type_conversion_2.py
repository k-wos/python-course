listData = [1,2,3,4,5,6]

tupleData = tuple(listData)
print(tupleData)

otherList = list(("Ola", 23, 234))

setData = set(otherList)
print(setData)


frozenSetData = frozenset(tupleData)
print(type(frozenSetData))
print(frozenSetData)

tupleData = (("Ola", 1234), ("Adam", 23643))

dictData = dict(tupleData)
print(dictData)