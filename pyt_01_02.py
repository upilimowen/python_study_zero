
a = int(input("Введите трехзначное число: "))
num3 = a//100
num2 = a%100//10
num1 = a%10
sum = num1 + num2 + num3
print(str(a) + " -> " + str(sum) + "(" + str(num3) + " + " + str(num2) + " + " + str(num1) + ")")

