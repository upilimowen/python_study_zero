a = int(input("Введите целое положительное число: "))
b = 1;
strResult = str(a) + " ->"
while ( a >= b):
    strResult = strResult + " " + str(b)
    b = b * 2;
print(strResult)

