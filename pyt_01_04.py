
a = int(input("Введите шестизначное число- номер: "))

exam = a%6

if (exam > 0):
    resultBoy = int(a//6)
    resultGirl = resultBoy * 4
    print(str(a) + " -> " + str(resultBoy) + "  " + str(resultGirl) + "  " + str(resultBoy) + " ( и помог учитель " + str(exam) + ")")
else:
    resultBoy = int(a / 6)
    resultGirl = resultBoy * 4
    print(str(a) + " -> " + str(resultBoy) + "  " + str(resultGirl) + "  " + str(resultBoy) )
