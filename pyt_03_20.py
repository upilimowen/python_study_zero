listOneEn = ["A", "E", "I", "O", "U", "L", "N", "S", "T", "R"]
listTwoEn = ["D", "G"]
listThreeEn = ["B", "C", "M", "P"]
listFourEn = ["F", "H", "V", "W", "Y"]
listFiveEn = ["K"]
listEightEn = ["J", "X"]
listTenEn = ["Q", "Z"]

listOneRu = ["А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"]
listTwoRu = ["Д", "К", "Л", "М", "П", "У"]
listThreeRu = ["Б", "Г", "Ё", "Ь", "Я"]
listFourRu = ["Й", "Ы"]
listFiveRu = ["Ж", "З", "Х", "Ц", "Ч"]
listEightRu = ["Ш", "Э", "Ю"]
listTenRu = ["Ф", "Щ", "Ъ"]

strA = str(input("Введите Ваше слово: "))

resultSum = 0

for i in range(len(strA)):
    strSymb = strA[i].upper()
    resultSum = resultSum + listOneEn.count(strSymb)
    resultSum = resultSum + 2 * listTwoEn.count(strSymb)
    resultSum = resultSum + 3 * listThreeEn.count(strSymb)
    resultSum = resultSum + 4 * listFourEn.count(strSymb)
    resultSum = resultSum + 5 * listFiveEn.count(strSymb)
    resultSum = resultSum + 8 * listEightEn.count(strSymb)
    resultSum = resultSum + 10 * listTenEn.count(strSymb)

    resultSum = resultSum + listOneRu.count(strSymb)
    resultSum = resultSum + 2 * listTwoRu.count(strSymb)
    resultSum = resultSum + 3 * listThreeRu.count(strSymb)
    resultSum = resultSum + 4 * listFourRu.count(strSymb)
    resultSum = resultSum + 5 * listFiveRu.count(strSymb)
    resultSum = resultSum + 8 * listEightRu.count(strSymb)
    resultSum = resultSum + 10 * listTenRu.count(strSymb)

print(str(resultSum))



