import random

numA = int(input("Введите число - количество монеток: "))
numB = 0
strResult = str(numA) + " ->";
numD = 0
numE = 0

while (numB < numA):
    numC = random.randint(0,1)
    strResult = strResult + " " + str(numC)
    if numC == 0:
        numD = numD + 1
    else:
        numE = numE + 1
    numB = numB + 1
print(strResult)
if (numD < numE) and (numD > 0):
    strResult = "Минимальное количество монеток - орлов: " + str(numD)
elif (numE > 0):
    strResult = "Минимальное количество монеток - решек: " + str(numE)
else:
    strResult = "Минимальное количество монеток - орлов: " + str(numD)
print(strResult)

