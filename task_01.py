# lesson_02 Задание 2 Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
#
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# БЫЛО
# num_us = int(input('Введите число N: '))
# list_ = []
#
# for i in range(num_us):
#     list_.append(i)
#     list_[i] = 1
#     for j in range(1, i+1):
#         list_[i] *= j + 1
#
# print(list_)

# СТАЛО
def f_(num):
    for i in range(1, num):
        num *= i
    return num

num_us = int(input('Введите число N: '))
list_ = [i for i in range(1, num_us+1)]
list_us = list(map(f_, list_))
print(list_us)
