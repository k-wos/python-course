setData = {2,3,1,4,5}
setData.add(10)

setData.discard(1)
print(type(setData))
print(setData)

for v in setData:
    print(v)
    
frozenData = frozenset(setData)
print(type(frozenData))