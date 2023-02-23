sizeA = int(input("Введите целое положительное число - количество элементов в массиве: "))
strA = str(input("Введите строку элементов в массиве: "))
listA = strA.split()
numX = int(input("Введите значение искомого числа: "))
diffA = abs(int(listA[0]) - numX);
result = str(listA[0])
if (len(listA) == sizeA):
    for i in range(len(listA)):
        numA = int(listA[i])
        diff = abs(numA - numX);
        if diff == 0:
            result = str(numA)
            break
        elif (diff < diffA):
            result = str(numA)
            diffA = diff
else:
    result = "Вы ввели рассогласованные данные!"

print("-> " + result)


