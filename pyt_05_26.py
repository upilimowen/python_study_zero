def expt(a, b):
    if b == 0:
        return 1
    else:
        return a * expt(a, (b-1))

numA = int(input("Введите Ваше число: "))
numB = int(input("Введите степень этого числа: "))

numResult = expt(numA, numB)

print("A = " + str(numA) + ",B = " + str(numB) + " => " + str(numResult))



