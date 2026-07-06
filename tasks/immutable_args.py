def increaseSalary(money, bonus):
    money += money * 0.2
    return money + bonus

salary = 5000
newSalary = increaseSalary(salary, 1000)

print(salary, newSalary)

def calculateFinalPrice(initialPrice, discount):
    newPrice = initialPrice - (initialPrice * (discount/100))
    return newPrice

newPrice = calculateFinalPrice(100, 10)
print(newPrice)

def calculateBMI(weight, height):
    return weight / ((height / 100) ** 2)

def classifyBMI(bmi):
    if bmi < 18.5:
        return print("Masz niedowagę")
    elif bmi < 25:
        return print("Twoja waga jest w normie")
    elif bmi < 30:
        return print("Masz nadwagę")
    else:
        return print("Masz sporą nadwagę")
    
height = 180
weight = 75

bmi = calculateBMI(height, weight)
result = classifyBMI(bmi)

