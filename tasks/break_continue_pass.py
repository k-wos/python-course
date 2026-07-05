data = [1,2,3,4,5,6,7,8,9,10]

for i in data:
    if i % 2 == 0:
        continue
    if i > 8:
        break
    if i % 2 != 0 and i <=8:
        print(i ** 2)
else:
    print("Koniec działania")