# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from os import sep
from unittest import result


n = int(input('Введите N: '))
fact_n = 1
for i in range(1, n + 1):
    fact_n *= i
    print(fact_n, end= ", ")