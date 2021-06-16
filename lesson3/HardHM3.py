# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
import math
equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y
equation1 = list(map(str,equation.split()))
y = float(equation1[2][:-1]) * x + float(equation1[4])
print(y)

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
# date = '01.11.1985'
#
# # Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'

date = list(map(str, input("Введите дату: ").split(".")))

if len(str(date[0])) != 2 or len(str(date[1])) != 2 or len(str(date[2])) != 4:
    print('Дата введена не корректно введите дату по примеру 01.01.0089')
elif (int(date[1]) == 2 or int(date[1]) == 4 or int(date[1]) == 6 or int(date[1]) == 9 or int(date[1]) == 11) \
        and int(date[0]) > 30 :
     print('вы ввели не правильную дату в этом месяце только 30 дней')
elif 0 < int(date[0]) <= 31 and 0 < int(date[1]) <= 12 and 0 < int(date[2]) <= 9999:
        print('Вы ввели правильную дату')
else:
    print('вы ввели не правильную дату')

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3
a = 13 #Номер квартиры которую задают жители
# здесь функция вычисления этажей
n = 0 # последовательность этажей с кратным числом квартир
s = 0 # номер последовательности
ss = 0 # максимальный этаж в последовательности
ls = []
ls_n = []
while a > n:
    s += 1
    n += s**2
    ss += s
    ls_n.append(int(n))
    ls.append(int(ss))
stage = ls[-2] + math.ceil((a - ls_n[-2])/s)
pos_kv = a - ls_n[-2]  # Можно проще разделить с остатком
while pos_kv > ss:
    pos_kv = pos_kv - ss
print(stage, pos_kv)