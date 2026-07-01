data = [0, 1, 2, 3, 4, 5, 6]

print(len(data))

del data[2];

print(len(data))

if 3 in data:
    print("3 jest w liście")
    
for el in data:
    print("element listy: ", el)
    
for el in data:
    print("element listy z wartościamy pomnożonymi przez 2", el * 2)