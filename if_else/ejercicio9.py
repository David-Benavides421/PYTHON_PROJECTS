num1 = int(input("Dime el numero 1:"))
num2 = int(input("Dime el numero 2:"))
num3 = int(input("Dime el numero 3:"))

if num1 > num2 and num1 > num3:
    if num2 > num3:
        print("El orden es:", num1, num2, num3)
    else:
        print("El orden es:", num1, num3, num2)
elif num2 > num1 and num2 > num3:
    if num1 > num3:
        print("El orden es:", num2, num1, num3)
    else:
        print("El orden es:", num2, num3, num1)
elif num3 > num1 and num3 > num2:
    if num1 > num2:
        print("El orden es:", num3, num1, num2)
    else:
        print("El orden es:", num3, num2, num1)