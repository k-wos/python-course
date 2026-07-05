def displayShoppingList(shoppingList):
    for i in shoppingList:
        print(i)
        

shoppingList = []

while True:
    product = input("Podaj produkt do listy: ")
    
    if product =="exit":
        break
    else:
        shoppingList.append(product)
        

displayShoppingList(shoppingList)