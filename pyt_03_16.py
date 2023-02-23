sizeA = int(input("Введите целое положительное число - количество элементов в массиве: "))
strA = str(input("Введите строку элементов в массиве: "))
listA = strA.split()
numX = str(input("Введите значение искомого числа: "))

if (len(listA) == sizeA):
    result = str(listA.count(numX))
else:
    result = "Вы ввели рассогласованные данные!"

print("-> " + result)


