def modifyStr(strData):
    print(id(strData))
    strData += "!"
    print(strData)
    print(id(strData))
    
string = "Hello"
print(id(string))
modifyStr(string)
print(string)


def modifyList(listData):
    print(id(listData))
    listData.append(10)
    print(id(listData))
    
listValue = [0,1,2]
print(id(listValue))

modifyList(listValue)