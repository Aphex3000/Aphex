# 6. Напишите функцию, которая принимает строку и возвращает количество гласных букв в ней
# def glas(stroka):
#     c = 0
#     for i in stroka:
#         if i in 'аяуюоеёэиы':
#             c += 1
#     return c
# stroka = 'Привет, как дела?'
# res = glas(stroka)
# print(res)

# 7. Напишите функцию, которая принимает два списка и возвращает список, содержащий элементы, общие для обоих списков.
# def my_list(list1, list2):
#     list_d = []
#     n = len(list1)
#     for i in list1:
#         if i in list1:
#             if i in list2:
#                 list_d.append(i)
#     return list_d
#
# list1 = [2, 5, 9, 11, 18, 32]
# list2 = [5, 9, 33, 48, 18, 120]
# res = my_list(list1, list2)
# print(res)

# 8. Напишите функцию, которая принимает список чисел и возвращает список, содержащий только уникальные элементы.
# def my_list(list1):
#     list_d = []
#     for elem in list1:
#         if elem in list_d:
#             continue
#         else:
#             list_d.append(elem)
#     return list_d
#
# list1 = [2, 5, 9, 11, 9, 32]
# res = my_list(list1)
# print(res)

# 9. Напишите функцию, которая принимает строку и возвращает количество слов в ней
# def my_list(list1):
#     count = 0
#     for elem in list1:
#         count += 1
#     return count
#
# list1 = [2, 5, 9, 11, 9, 32, 10]
# res = my_list(list1)
# print(res)

# 10. Напишите функцию, которая принимает список строк и возвращает самую длинную строку из списка.
# def my_list(list1):
#     max1 = max(list1, key=len)
#     for i in list1:
#         if i == max1:
#             max1 = i
#     return max1
#
# list1 = ['стол', 'клавиа', 'тумбочка', 'светильник']
# res = my_list(list1)
# print(res)

# 11. Напишите функцию, которая принимает число и возвращает его факториал.
# def fact(number):
#     if number ==1:
#         return 1
#     return fact(number - 1) * number
#
# number = 4
# res = fact(number)
# print(res)


# 12. Напишите функцию, которая принимает список чисел и возвращает список, содержащий квадраты этих чисел.
# def my_list(list1):
#     list2 = []
#     for elem in list1:
#         elem = elem ** 2
#         list2.append(elem)
#     return list2
#
# list1 = [2, 5, 9, 11, 9, 32, 10]
# res = my_list(list1)
# print(res)

# 13. Напишите функцию, которая принимает число и проверяет, является ли оно палиндромом (читается одинаково слева направо и справа налево).
# def palindrom(number):
#     s = str(number)
#     return s == s[::-1]
#
# number = 535535
# res = palindrom(number)
# print(res)


# 14. Напишите функцию, которая принимает список строк и возвращает список, содержащий только уникальные строки.
# def my_list(list1):
#     list_d = []
#     for elem in list1:
#         if elem in list_d:
#             continue
#         else:
#             list_d.append(elem)
#     return list_d
#
# list1 = ['ff', 'ff', 'r', 'b', 'ww', 't']
# res = my_list(list1)
# print(res)