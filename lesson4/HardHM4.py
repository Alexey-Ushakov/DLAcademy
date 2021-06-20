# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3
# a = input("Введите дроби через пробел: ")
a = 5/6 + 4/7
a = a.split()

a[0] = a[0].split("/")
a[2] = a[2].split("/")
b = ["1"]
if len(a[0]) == 1:
    a[0] = list(a[0])
    a[0] = a[0] + b
if len(a[2]) == 1:
    a[2] = list(a[2])
    a[2] = a[2] + b


if a[1] == "+":
    obch_chislitel = int(a[0][0]) * int(a[2][1]) + int(a[0][1]) * int(a[2][0])
    obch_znam = int(a[0][1]) * int(a[2][1])
    celai = obch_chislitel // obch_znam
    drobnai = abs(obch_chislitel % obch_znam)
elif a[1] == "-":
    obch_chislitel = int(a[0][0]) * int(a[2][1]) - int(a[0][1]) * int(a[2][0])
    obch_znam = int(a[0][1]) * int(a[2][1])
    celai = obch_chislitel // obch_znam
    drobnai = abs(obch_chislitel % obch_znam)
print("{} {}/{}".format(celai,drobnai,obch_znam ))


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
import os
path = os.path.join("data", "hours_of.txt")
f = open(path, encoding="UTF-8" )
# with open("data", "hours_of.txt") as read_file:
#     read_file.read()
b = f.readlines()
new_b = []
for i in b:
    i = i.split()
    new_b.append(i)
f.close
new_b[0][2] = "Отработано часов"
del new_b[0][3]
# for i in new_b:
#     for j in i:
#         print(j)
path = os.path.join("data", "workers.txt")
f = open(path, encoding="UTF-8" )
w = f.readlines()
new_w = []
for i in w:
    i = i.split()
    new_w.append(i)
f.close
# print(new_b)
# print(new_w)
new_a = []
new_b = sorted(new_b)
new_w = sorted(new_w)
i = 0
while i < len(new_w):
    new_w[i].append(new_b[i][2])
    i += 1
del new_w[3]
for i in new_w:
    if int(i[4]) > int(i[5]):
        a =int((int(i[2]) / int(i[4])) * (int(i[5])))
        i.append(a)
    elif int(i[4]) <= int(i[5]):
        a = int(int(i[2]) + ((int(i[5]) - int(i[4])) * 2 * (int(i[2]) / int(i[4]))))
        i.append(a)
for i in new_w:
    print(i)



# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))