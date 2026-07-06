number = 12

def test1():
    print(number)
    
test1()

def test2():
    number = 100
    print(number)
    if 1 == 1:
        print(number)
    if 2 == 2:
        number = 50
        print(number)
    print(number)
    
test2()
print(number)

print("\ntest3")

def test3():
    global number 
    number = 5
    print(number)
    
test3()
print(number)

print("\ntest4")

number = 10
def test4(number):
    print(number)
    number = 20
    print(number)
    
test4(15)
print(number)

print("\ntest5")

number = 10
def foo():
    print(number)
    
def bar():
    number = 9
    print(number)
    foo()
    
bar()

print("\ncheck1 & check2")

number = 10

def check1():
    number = 9
    print(number)
    def check2():
        print(number)
    check2()
    
check1()