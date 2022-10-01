# Реализуйте алгоритм перемешивания списка.

# list_num = input('Введите ряд цифр: ')
# print(', '.join(list_num))
# print(list_num[0])
# n = 1
# while n < len(list_num) / 2:
#     temp = list_num[0]
#     list_num[0] = list_num[-1]
#     list_num[-1] = temp
#     n += 1
# print(', '.join(list_num))

list_num = input('Введите ряд цифр: ')
print(f'{list_num[len(list_num)//2:]}{list_num[:len(list_num)//2]}')