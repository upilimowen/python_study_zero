def its_prime_number(number):
    b = number
    while b > 2:
        b = b - 1
        if number % b == 0:
            return False
    return True

try:
    a = int(input("Введите Ваше число: "))
    b = a
    print(b)
    string_result = "Простые множители числа " + str(a) + " : " + str(b)
    while b > 2:
        b=b-1
        if a%b == 0:
            if its_prime_number(b):
                string_result = string_result + ", " + str(b)
    string_result = string_result + ", 1."
    print(string_result)
except:
    print("Я ничего не понял.")