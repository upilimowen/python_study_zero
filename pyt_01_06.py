
a = int(input("Введите шестизначное число - номер билета: "))

if (a < 100000) or (a > 999999):
    print(" Это не шестизначный номер! ")
else:
    num6 = a // 100000
    num5 = a % 100000 // 10000
    num4 = a % 10000 // 1000
    num3 = a % 1000 // 100
    num2 = a % 100 // 10
    num1 = a % 10
    sum1 = num6 + num5 + num4
    sum2 = num3 + num2 + num1
    if (sum1 == sum2):
        print(str(a) + " -> yes")
    else:
        print(str(a) + " -> no")