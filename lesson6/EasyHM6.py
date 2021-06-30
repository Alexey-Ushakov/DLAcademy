# Задача-1:
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:
def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.
    """
    return (a * b) ** 0.5
while True:
    try:
        a = float(input("a = "))
        b = float(input("b = "))
        c = avg(a, b)
    except ValueError:
        print("Введите число без посторонних символов и букв")
    else:
        print("Среднее геометрическое = {:.2f}".format(c))
        break

# ПРИМЕЧАНИЕ: Для решения задач 2-4 необходимо познакомиться с модулями os, sys!
# СМ.: https://pythonworld.ru/moduli/modul-os.html, https://pythonworld.ru/moduli/modul-sys.html

import os
import sys

# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
def make_dir(derectory):

    try:
        if os.path.exists(derectory):
            raise Exception("Это папка уже есть")
        else:
            os.mkdir(derectory)
    except Exception as e:
        print(e)
    else:
        print("дириктория {} создана".format(derectory))




for i in range(1, 10):
    derectory = "dir_" + str(i)
    make_dir(derectory)

print(os.listdir(os.path.dirname(__file__)))


def make_del_dir(derectory):
    try:
        if not os.path.exists(derectory):
            raise Exception("Нет такой папки")
        else:
            os.rmdir(derectory)
    except Exception as e:
        print(e)
    else:
        print("дириктория {} удалена".format(derectory))


for i in range(1, 10):
    derectory = "dir_" + str(i)
    make_del_dir(derectory)


# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.

print(os.listdir(os.path.dirname(__file__)))

# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import sys
import os
import shutil
from os import path

src = path.realpath(__file__)
head, tail = path.split(src)
dst = src + ".bak"
shutil.copy(src, dst)

print(os.listdir(os.path.dirname(__file__)))






# destdir = os.path.abspath('destdir')
# if not os.path.exists(destdir):
#     os.makedirs(destdir)

# # с использованием системного shell'а
# os.system('copy %s %s' % (__file__, destdir))
# # другой вариант - с получением полного имени скрипта через sys.argv[0]
# os.system('copy %s %s' % (sys.argv[0], destdir))
#
# # без shell'а
# dirname, filename = os.path.split(__file__)
# content = open(__file__).read()
# open(os.path.join(destdir, filename), 'w').write(content)
#
# from shutil import copyfile, copy
#
# copy(__file__, destdir)  # копируем в указанную директорию
# copyfile(__file__, os.path.join(destdir, filename))  # копируем по полному пути нового расположения

