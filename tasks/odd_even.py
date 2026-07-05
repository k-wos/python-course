numbers = [-4,-3,-2,-1,0,1,2,3,4]

for v in numbers:
    if v == 0:
        print("Zero jest parzyste")
    elif v % 2 == 0:
        print(str(v) + " jest parzysta")
    else:
        print(str(v) + " jest nieparzysta")