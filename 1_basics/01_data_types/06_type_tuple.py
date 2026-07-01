data = ("Ala", "Ola", "Natalia")
# data[0]= "Rafał" błąd

names = data + ("Rafał", )

print(names)
print(len(names))
print(type(names))

numbers = 1, 2 , 3
print(type(numbers))

emptyTuple = ()
print(type(emptyTuple))

print(names[1])
print(names[-1])
print(names[1:])

cars = (("dodge", "ford"), ("porsche"))
print(cars[0][0])

if "ford" in cars[0]:
    print("Ford w krotce")
    
del cars

tupleX3 = names * 3
print(tupleX3)