# lesson_02 Задание 3 Задайте список из n чисел последовательности
# (1+1/n)^n и выведите на экран их сумму,
# округлённую до трёх знаков после точки.
#
# Пример:
# Для n = 6 -> 14.072

# БЫЛО:
# num_us = int(input('Введите число n: '))
#
# list_ = []
# for i in range(num_us + 1):
#     list_.append(i)
#     if i == 0:
#         list_[i] = 0
#     else:
#         list_[i] = (1 + 1/i) ** i
#
# summ_ = 0
# for j in range(num_us + 1):
#     summ_ += list_[j]
#
# print(num_us, '->>', round(summ_, 3))

# СТАЛО:
def summ_list(lst):
    summ_ = 0
    for j in range(len(lst)):
        summ_ += lst[j]
    return summ_


num_us = int(input('Введите число n: '))
f_ = lambda x: (1 + 1/x) ** x
list_ = [f_(i) for i in range(1, num_us+1)]
summ_ = summ_list(list_)
print(num_us, '->>', round(summ_, 3))
