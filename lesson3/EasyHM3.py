# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
list_of_fruits = ["яблоко", "банан", "киви", "арбуз"]
for i in list_of_fruits:
    print(str(list_of_fruits.index(i) + 1)+".", "{:>10}".format(i))


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
list1 = [1, 2, 3, 4, 3, 3, 5]
list2 = [2, 3, 6, 8, 7, 4, 8, 10, 56]
new_list = []
for i in list1:
    if i not in list2:
        new_list.append(i)
print(new_list)



# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
list_chisel = [2, 4, 8, 10, 13, 3, 7]
new_list1 = []
for i in list_chisel:
    if i % 2 == 0:
        i /= 4
        new_list1.append(i)
    else:
        i *= 2
        new_list1.append(i)
print(new_list1)

