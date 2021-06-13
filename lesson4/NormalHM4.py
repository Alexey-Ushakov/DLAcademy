import math
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fib1 = 1
    fib2 = 1
    z = 0
    while m != z:
        z += 1
        fib1, fib2 = fib2, fib1 + fib2
        if z >= n:
            print(fib1, fib2)


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    i = 0
    while i < (len(origin_list) - 1):
        j = 0
        while j < (len(origin_list) - 1) - i:
            if origin_list[j] > origin_list[j + 1]:
                origin_list[j], origin_list[j + 1] = origin_list[j + 1], origin_list[j]
            j += 1
        i += 1
    print(origin_list)

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(my_filter, array):
    result = []
    for elem in array:
        if my_filter(elem):
            result.append(elem)
    return result

# тут клевая функция работающая через булевую логику


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def parallelogran(x1,x2,x3,x4,y1,y2,y3,y4):
    ab = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    bc = math.sqrt((x2 - x3)**2 + (y2 - y3)**2)
    cd = math.sqrt((x3 - x4)**2 + (y3 - y4)**2)
    da = math.sqrt((x4 - x1)**2 + (y4 - y1)**2)

    bd = math.sqrt((x2 - x2)**2 + (y2 - y2)**2)
    ac = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
    if (ab == cd and bc == da) or (ab == cd and bd == ac):
        return True
    else:
        return False
print(parallelogran(1,5,5,1,1,1,8,8))

# №5 напишите свою идеальную функцию
def idealnia_func():
    pass