# Напишите функцию, которая принимает строку и выводит на экран все символы этой строки в обратном порядке.
def x(stroka):
    k = ''
    n = len(stroka)
    for i in range(n):
        i1 = stroka[::-1]
        k += i1
        break
    return k
my_stroka = 'Привет'
res = x(my_stroka)
print(res)

# Напишите функцию, которая принимает число и выводит на экран таблицу умножения для этого числа от 1 до 10.
def x(number):
    for i in range(1, 11):
        print(number, 'x', i, '=', number * i)

my_number = 6
res = x(my_number)

# Напишите функцию, которая принимает список чисел и возвращает новый список, содержащий квадраты четных чисел
def x(spisok):
    new_spisok = []
    for i in spisok:
        if i % 2 == 0:
            n = i ** 2
            new_spisok.append(n)
    return new_spisok
my_spisok = [123, 456, 852, 789, 456 , 489]
res = x(my_spisok)
print(res)