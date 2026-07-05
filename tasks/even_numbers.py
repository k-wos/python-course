numTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for i in numTuple:
    if i % 2 == 0:
        print(str(i) + " jest parzysta")
    else:
        print(str(i) + " jest nieparzysta, a reszta z dzielenia wynosi: " + str(i % 2))