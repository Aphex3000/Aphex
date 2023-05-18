# напиши функцию, кооторая принимает список чисел , а вернет сумму квадратов эл-тов
def sum_(spisok):
    s = 0
    for i in spisok:
        k = i ** 2
        s += k  # да к
    return s

myspisok = [2, 4, 7, 10, 15]
res = sum_(myspisok)
print(res)


# напиши функцию, кооторая принимает список чисел , а вернет сумму последних цифр

def sum_(spisok):
    s = 0
    for i in spisok:
        k = i % 10
        s += k
    return s

myspisok = [2, 4, 7, 10, 15]
res = sum_(myspisok)
print(res)


# напиши функцию, кооторая принимает список строк, а вернет  список с первыми символами этих строк

def sum_(spisok):
    spisok1 = []
    for i in spisok:
        k = i[0]
        spisok1.append(k)
    return spisok1

myspisok = ['werwe', 'fgfg', 'jhgj', 'hfghfgh', 'wrfewfw']
res = sum_(myspisok)
print(res)


# напиши функцию, кооторая принимает список строк, а вернет  список со склеиными первой  и последний символов. если строка длины 1, то пропустить

def sum_(spisok):
    spisok1 = []
    for i in spisok:
        if len(i) == 1:
            continue
        k = i[0]
        n = i[-1]
        spisok1.append(k + n)
    return spisok1

myspisok = ['werwe', 'fgfg', 'jhgj', 'hfghfgh', 'wrfewfw']
res = sum_(myspisok)
print(res)


# напиши функцию, кооторая принимает список строк "yes" или "no", а вернет число являющейся суммой следующего ("yes" это 1, "no" это -1)   ['yes', 'yes'] => 1+1=2   ['no', 'no', 'yes'] => -1-1+1=-1
def sum_(spisok):
    s = 0
    for i in spisok:
        if i == 'yes':
            s += 1
        else:
            s -= 1
    return s

myspisok = ['yes', 'no']
res = sum_(myspisok)
print(res)


# напиши функцию, кооторая принимает множество чисел, а вернет список упорядоченных чисел

def sum_(mnogestvo):
    return sorted(mnogestvo)

my_mnogestvo = {1151, 4546, 4545, 4546}
res = sum_(my_mnogestvo)
print(res)