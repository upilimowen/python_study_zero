numA = int(input("Введите число - сумму: "))
numB = int(input("Введите число - произведение: "))
numC = numA//2
numD = 0
numE = numA
result = False
strResult = str(numA) + " " + str(numB) + " -> "
while (numD <= numC):
    numE = numA - numD
    if ((numE * numD) == numB):
        result = True
        break
    numD = numD + 1
if result:
    strResult = strResult + " " + str(numD) + " " + str(numE)
else:
    strResult = "Для таких условий задачи - решений нет."
print(strResult)

