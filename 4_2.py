try:
    string_input = ""
    string_result = ""
    spisok = []
    while string_input != "Стоп":
        string_input = input("Введите натуральное число, для того чтобы остановиться - введите слово ""Стоп"": ")

        if string_input != "Стоп":
            try:
                number = int(string_input)
                gg = spisok.count(string_input)
                if gg == 0:
                   spisok.append(string_input)
                   string_result = string_result + " || " +string_input
            except:
                print("Это не число и не слово ""Стоп"".")
    print(string_result)
except:
    print("Я ничего не понял.")