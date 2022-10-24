# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11  

# Var my
# n = input("Введите дробное: ")
 
# suma_n = 0
 
# for figure in n:
#     if figure.isdigit():  # insdigit()  -  проверка позиции на цифру
#         suma_n += int(figure)
 
# print("Сумма цифр равна:", suma_n)


# Var 2

# n = list(input("Введите дробное: ")) #
# sum_dig = 0

# for i in range(len(n)):    # пробегаем по ряду длиной  n
#     if n[i] == '.':        # если позиция равна "." ->
#         continue           # -> переходим в начало цикла
#     sum_dig += int(n[i])
# print(sum_dig)

# Var with List comprehension

from unicodedata import digit


n = list(input("Введите дробное: "))
sum_1 = sum([int(digit) for digit in n if digit.isdigit()])
print(sum_1)