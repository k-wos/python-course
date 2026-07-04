text = "Hello"
print(text.upper())

x = 256
y = 256

print (x is y)

listOne = [1,3,4,5]
listTwo = listOne

print (listOne is listTwo)

listOne.append(4)
if listOne is listTwo:
    print("Modyfikacja wpłynęła też na listTwo")