list = ["Ola", "Ania", 23, 99, "Rafał"]

print(type(list))
print(list)

print(list[0])
print(len(list))
print(list[4])
print(list[len(list)-1])

print(list[-1])

print(list[1:4])
print(list[2:])

list[0] = "Natalia"
print(list)

del list[2]
print(list)

print(99 in list)
print(11 in list)

if("Ania" in list):
    print("Ania jest w liście list")
    print("Kolejny Kod")
    
    for v in list:
        print(v)
        
data = [
    ["Daniel", "Rafał"],
    ["Natalia", "Ania"],
    ["Ola", "Adam"]
    ]

print(len(data))
print(data[1][0])

data1 = [1, 2, 3]
data2 = [4, 5, 6]

numbers = data1 + data2

print(numbers)
numbersX2 = numbers * 2
print(numbersX2)