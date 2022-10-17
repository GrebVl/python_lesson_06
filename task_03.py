# lesson_02 Задание 4 Задайте список из N элементов,
# заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.

# БЫЛО
# N = int(input('Введите число N: '))
# a = int(input('Введите число a: '))
# b = int(input('Введите число b: '))
#
# list_ = []
#
# for i in range(-N, N+1):
#     list_.append(i)
#
# product_numbers = list_[a-1] * list_[b-1]
#
# print(list_)
# print('a ->>', list_[a-1], 'b ->>', list_[b-1])
# print(product_numbers)

# СТАЛО
list_N_a_b = list(map(int, input('Введите число N, a, b, через пробел: ').split()))
N = list_N_a_b[0]
a = list_N_a_b[1] - 1
b = list_N_a_b[2] - 1
list_ = [i for i in range(-N, N + 1)]

print(list_)
print('a ->>', list_[a], 'b ->>', list_[b])
print(list_[a] * list_[b])
