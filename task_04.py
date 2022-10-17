# lesson_04 Задайте 3 последовательность чисел.
# Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.
#
# *Пример*
# - при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]  -> [2, 4, 5, 9]

# list_us = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]
# list_duoble = []
# for i in range(len(list_us)):
#     count = 0
#     for j in range(1, len(list_us)):
#         if count >= 1:
#             break
#         elif list_us[i] == list_us[j] and i != j:
#             list_duoble.append(list_us[i])
#             count += 1
#
#
# print('Первичный список элиментов: ', list_us)
# print('Повторяющиеся элименты', list_duoble)
# #
# # for k in range(len(list_duoble)):
# #     val_ = list_duoble[k]
# #     while val_ in list_us:
# #         list_us.remove(val_)
#
#
#
# print('Список неповторяющихся элементов: ', list_us)


def filter_list(list_):
    if list_ in list_duoble:
        return False
    else:
        return True

list_us = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]
print('Первичный список элиментов: ', list_us)

list_duoble = []
for i in range(len(list_us)):
    count = 0
    for j in range(1, len(list_us)):
        if count >= 1:
            break
        elif list_us[i] == list_us[j] and i != j:
            list_duoble.append(list_us[i])
            count += 1

lst_filter = list(filter(filter_list, list_us))
print('Список неповторяющихся элементов: ', lst_filter)