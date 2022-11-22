from random import randint
max_koeff = 100
k = int(input("Введите натуральную степень k:"))
koeff = [randint(0,max_koeff) for i in range(k)]+[randint(1,max_koeff)]
string_result = '+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(koeff) if j][::-1])
string_result = string_result.replace('x^1+', 'x+')
string_result = string_result.replace('x^0', '')
string_result += ('','1')[string_result[-1]=='+']
string_result = (string_result, string_result[:-2])[string_result[-2:]=='^1']
print(string_result)