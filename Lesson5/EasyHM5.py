# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
# ls_1 = [1, 2, 4, 0]
# ls_2 = []
# for i in ls_1.copy():
#     i *= i
#     ls_2.append(i)
# print(ls_2)


# for i in range(0,10,2):
#     ls_1.append(i)
# for i in ls_1.copy():
#     i = i * i
#     ls_2.append(i)
# print(ls_1, ls_2)

ls_1 = [i for i in range(0, 10, 2)]
ls_2 = [i * i for i in ls_1]
print(ls_2)


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
ls_f1 = ["apple", "banan", "tomato", "pear", "blueberries", "Gooseberries"]
ls_f2 = ["apple", "banan", "tomato", "avocado", "Cherries", "Grapefruit", "Gooseberries"]
ls_f3 =[]
for i in ls_f1.copy():
    for j in ls_f2.copy():
        if j == i:
            ls_f3.append(i)
print(ls_f3)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
import random
my_list = [random.randint(-100, 100) for i in range(0, 100)]
# my_list =[my_list.append(i) for i in my_list if i % 3 == 0 or i > 0 or i %4 == 0]
my_list1 = []
print(my_list)
for i in my_list.copy():
    if i % 3 == 0 and i > 0 and i % 4 == 0:
        my_list1.append(i)
print(my_list1)