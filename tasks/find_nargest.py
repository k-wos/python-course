def findLargest(num1, num2):
    if num1 > num2:
        return print("num1 jest większe: " + str(num1))
    elif num2 > num1:
        return print("num2 jest większe: " + str(num2))
    else:
        return print("Obie liczby są równe")
    
findLargest(3, 10)
findLargest(12, 7)
findLargest(10, 10)