listSymbols = ["а", "я", "у", "ю", "о", "е", "ё", "э", "и", "ы"]
strPuh = str(input("Напишите кричалку: "))
listPuh = strPuh.split()
strAnswer = "Парам пам-пам"

i = 0
countFirst = 0
while i < len(listPuh):
    phrasePuh = listPuh[i].lower()
    i = i + 1
    j = 0
    countPuh = 0
    while j < len(phrasePuh):
        strSymb = phrasePuh[j]
        j = j + 1
        countPuh = countPuh + listSymbols.count(strSymb)
    if i == 1:
        countFirst = countPuh
    else:
        if (countFirst != countPuh):
            strAnswer = "Пам парам"
print(str(strAnswer))


