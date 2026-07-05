endOfRange = int(input("Podaj koniec zakresu:"))
evenNumbers = []
oddNumbers = []

for v in range(1, endOfRange + 1):
    if v % 2 == 0:
        evenNumbers.append(v)
    else:
        oddNumbers.append(v)
        
print("Parzysta lista: ", evenNumbers)
print("Nieparzysta lista: ", oddNumbers)