employees = []

def addEmployee(email, salary):
    employee = {
        "email": email,
        "salary": salary
    }
    employees.append(employee)
    
addEmployee("adam@example.com", 6000)
addEmployee("andrzej@example.com", 8000)
addEmployee("tomasz@example.com", 10000)
    
def increaseSalary(employees, pctIncrease):
    pctIncrease *= 0.01
    
    for e in employees:
        e["salary"] *= 1+ pctIncrease
        
increaseSalary(employees, 20)
print(employees)


accountBalance = 0

def addFunds(amount):
    global accountBalance
    accountBalance += amount
    
def withdrawFunds(amount):
    global accountBalance
    if accountBalance <=0:
        print("Nie można wypłacić")
    else:
        accountBalance -= amount

def displayBalance():
    print(accountBalance)
    
while True:
    action = input("Podaj działanie")
    if action == "dodaj":
        amount = int(input("Podaj ile wplacasz: " ))
        addFunds(amount)
    if action == "wyplac":
        amount = int(input("Podaj ile wyplacasz: " ))
        withdrawFunds(amount)
    if action == "pokaz":
        displayBalance()
    if action == "koniec":
        break