import sys
import os
import shutil
from os import path

# Задача-1:
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:

# def avg(a, b):
#     """Вернуть среднее геометрическое чисел 'a' и 'b'.
#
#     Параметры:
#         - a, b (int или float).
#
#     Результат:
#         - float.
#     """
#     return (a * b) ** 0.5
#     while True:
#         try:
#             a = float(input("a = "))
#             b = float(input("b = "))
#             c = avg(a, b)
#         except ValueError:
#             print("Введите число без посторонних символов и букв")
#         else:
#             print("Среднее геометрическое = {:.2f}".format(c))
#             break

# ПРИМЕЧАНИЕ: Для решения задач 2-4 необходимо познакомиться с модулями os, sys!
# СМ.: https://pythonworld.ru/moduli/modul-os.html, https://pythonworld.ru/moduli/modul-sys.html

import os
import sys

def look_dir():
    return os.listdir(os.path.dirname(__file__))

# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def make_dir(derectory):
    if not derectory:
        print("Укажите диреторию вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), derectory)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(derectory))
    except FileExistsError:
        print('директория {} уже существует'.format(derectory))


for i in range(1, 10):
    derectory = "dir_" + str(i)
    make_dir(derectory)

print(look_dir())


def make_del_dir(derectory):
    if not derectory:
        print("Укажите диреторию вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), derectory)
    try:
        os.rmdir(dir_path)
        print('директория {} удалена'.format(derectory))
    except FileExistsError:
        print('директория {} не существует'.format(derectory))

for i in range(1, 10):
    derectory = "dir_" + str(i)
    make_del_dir(derectory)


# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.



print(look_dir())

# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.



def file_copy():
    current_dir_file = path.realpath(__file__)
    current_dir, file_name = path.split(current_dir_file)
    name, extension = str(file_name).split(".")
    new_file = os.path.join(current_dir, (name + 'copy'+"." + extension))
    if not os.path.exists(new_file):
        shutil.copy(current_dir_file, new_file)
        print(new_file + ' - создан')
    else:
        print('Файл уже скопирован')

file_copy()

print(look_dir())







