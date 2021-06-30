import re
# Задание-1:
# Матрицы в питоне реализуются в виде вложенных списков:
# Пример. Дано:
matrix = [[1, 0, 8],
          [3, 4, 1],
          [0, 4, 2]]


# Выполнить поворот (транспонирование) матрицы
# Пример. Результат:
# matrix_rotate = [[1, 3, 0],
#                  [0, 4, 4],
#                  [8, 1, 2]]

# Суть сложности hard: Решите задачу в одну строку
matrix_1 = list(map(list, (zip(*matrix))))

# Задание-2:
# Найдите наибольшее произведение пяти последовательных цифр в 1000-значном числе.
# Выведите произведение и индекс смещения первого числа последовательных 5-ти цифр.
# Пример 1000-значного числа:
number = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""


list_of_number = []
for i in range((len(number)) - 4):
    pattern = "^\d{5}"
    number_new = number.replace(r"\n", "")
    number_new = number[i:]
    chisla = re.findall(pattern, number_new)
    list_of_number = list_of_number + chisla

max_mylti = 1
mylti = 1
index = 0
for i in list_of_number:
    for j in list(i):
       mylti = mylti * int(j)
    if mylti > max_mylti:
        max_mylti = mylti
        mylti = 1
        index = i
    else:
        mylti = 1
print(max_mylti, number.find(index))



# Задание-3 (Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
first = list(input("Введите пару чисел:").split(" "))
second = list(input("Введите пару чисел:").split(" "))
third = list(input("Введите пару чисел:").split(" "))
fourth = list(input("Введите пару чисел:").split(" "))
fifth = list(input("Введите пару чисел:").split(" "))
sixth = list(input("Введите пару чисел:").split(" "))
seventh = list(input("Введите пару чисел:").split(" "))
eighth = list(input("Введите пару чисел:").split(" "))
list_of_chess = [first, second, third, fourth, fifth, sixth, seventh, eighth]

i = 0
while i < len(list_of_chess):
    list_of_chess[i] = [int(j) for j in list_of_chess[i]]
    i = i + 1

list_of_chess_x = []
list_of_chess_y = []
for i in range(len(list_of_chess)):
    x_tmp = list_of_chess[i][0]
    list_of_chess_x.append(x_tmp)
    y_tmp = list_of_chess[i][1]
    list_of_chess_y.append(y_tmp)
a = True
if a:
    for i in list_of_chess_x:
        n = list_of_chess_x.count(i)
        if n >= 2:
            a = False
            break
        for j in list_of_chess_y:
            n = list_of_chess_y.count(i)
            if n >= 2:
                a = False
                break
    i = 0
    while i < (len(list_of_chess) - 1):
        j = 0
        while j < (len(list_of_chess) - 1) - i:
            if abs(list_of_chess[j][0] - list_of_chess[j + 1][0]) == abs(list_of_chess[j][1] - list_of_chess[j + 1][1]):
                a = False
                break
            else:
                list_of_chess[j], list_of_chess[j + 1] = list_of_chess[j + 1], list_of_chess[j]
            j += 1
        i += 1
    print("Yes")
else:
    print("No")