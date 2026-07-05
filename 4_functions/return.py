def addNumbers(a,b,c):
    return a + b + c

def sumListElements(listData):
    if len(listData) == 0:
        print("Pusta lista")
        return None
    result = 0
    for i in listData:
        result += i
    return result


print(sumListElements([]))
print(sumListElements([1,2,3]))

def printList(listData):
    if len(listData) == 0:
        return
    for v in listData:
        print(v)
        
printList([])
printList([1,23,4,5])