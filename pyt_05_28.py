def sum(a, b):
    if b == 1:
        return a + 1
    else:
        a = a + 1
        return sum(a, (b - 1))

numA = int(input("Введите первое неотрицательное число: "))
numB = int(input("Введите второе неотрицательное число: "))

numResult = sum(numA, numB)

print(str(numA) + " + " + str(numB) + " = " + str(numResult))



