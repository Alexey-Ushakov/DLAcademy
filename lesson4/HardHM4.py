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

def func_list_drob(element):
    """
    Возвращает список дроби где нулевой и первый элемент числитель и знаменатель целой частиБ второй и третий элемент
    числитель и знаменатель дробной части
    :param element: Исходная дробь
    :return: Список целых чисел
    """
    cel_chast = "0"
    drobn_chast = "0"
    list_1 = element.split()

    if len(list_1) == 2:
        cel_chast = list_1[0]
        drobn_chast = list_1[1]
    else:
        if '/' in list_1[0]:
            drobn_chast = list_1[0]
        else:
            cel_chast = list_1[0]
    list_cel_chast = [cel_chast, "1"]

    if drobn_chast == "0":
        list_drob_chast = ["0", "1"]
    else:
        list_drob_chast = drobn_chast.split("/")
    list_of_drob = [int(i) for i in list_cel_chast+list_drob_chast]
    # list_of_drob = list(map(int,list_cel_chast+list_drob_chast))
    return list_of_drob

def obshai_drob(element):
    """
    Возвращает список где нулевой элемент числитель дроби содержащий целую часть и первый элемент знаменатель дроби
    :param element: исходная дробь с целочисленной частью или без нее
    :return:
    """
    if element[0] < 0:
        obsh_chislitel = element[0] * element[3] - element[2] * element[1]
    else:
        obsh_chislitel = element[0] * element[3] + element[2] * element[1]
    obch_znamenatel = element[1] * element[3]
    list_obshai_drob = [obsh_chislitel, obch_znamenatel]
    return list_obshai_drob


drob = "5/6 - 2/8"
SIGN_PLUS = " + "
SIGN_MINUS = " - "
sign = "+"
if SIGN_PLUS in drob:
    drob_exp = drob.split(SIGN_PLUS)
else:
    drob_exp = drob.split(SIGN_MINUS)
    sign = "-"

first_drob = drob_exp[0]
second_drob = drob_exp[1]
first_drob = func_list_drob(first_drob)
second_drob = func_list_drob(second_drob)
first_drob = obshai_drob(first_drob)
second_drob = obshai_drob(second_drob)

if sign == "-":
    vicheslenie_chislitl_drobi = first_drob[0] * second_drob[1] - second_drob[0] * first_drob[1]
else:
    vicheslenie_chislitl_drobi = first_drob[0] * second_drob[1] + second_drob[0] * first_drob[1]
vicheslenie_znamenatel_drobi = first_drob[1] * second_drob[1]

print("{}{} {}/{}".format("" if vicheslenie_chislitl_drobi >= 0 else '-',
                          "" if abs(vicheslenie_chislitl_drobi) // vicheslenie_znamenatel_drobi ==0
                          else abs(vicheslenie_chislitl_drobi) // vicheslenie_znamenatel_drobi,
                          abs(vicheslenie_chislitl_drobi) % vicheslenie_znamenatel_drobi,
                          vicheslenie_znamenatel_drobi))


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

import os
path_fruits = os.path.join("data","fruits.txt")  # Указываем путь к файлу
with open(path_fruits, 'r', encoding='UTF-8') as f:  # Открываем его как f
    for i in f:
        for item in list(map(chr, range(ord('А'), ord('Я') + 1))):  # Пробегаем по алфавиту и сравниваем первую букву
            # строки с буквой в алфавите
            if item == (i)[0:1:]:
                file_name ="fruits_" + item + '.txt'
                path = os.path.join("data", file_name)
                with open(path, 'a+', encoding="UTF-8") as f:
                    f.write(i)
