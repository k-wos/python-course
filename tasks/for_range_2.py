endOfRange = int(input("Podaj koniec zakresu:"))
result = []

for v in range(1, endOfRange + 1):
    result.append(v ** 2)
    
if len(result) > 0:
    print ("Lista kwadratów liczb od 1 do " + str(endOfRange) + ": ", result)