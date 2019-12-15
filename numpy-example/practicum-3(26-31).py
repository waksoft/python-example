"""
Имя проекта: Boring-numpy
Номер версии: 1.0
Имя файла: practicum-3(26-31).py
Автор: 2019 © В.В. Костерин, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)

Дата создания: 07/12/2019
Дата последней модификации: 15/12/2019

Связанные файлы/пакеты: numpy, random

Описание: Решение задач №№ 26-31 практикума № 3

#версия Python: 3.6
"""
import numpy as np
import random as rnd

"""
26. Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
случайными элементами. Дан номер строки L и номер столбца K, при
помощи которых исходная матрица разбивается на четыре части. Найти
среднее арифметическое элементов каждой части.
"""
print("\n\nЗадача №26")
N = 6    # строк
M = 10    # колонок
print("Строк N = ", N, "\nКолонок M = ", M)

L = 2
K = 4
print("Строка для разделения L = ", L, "\nКолонка для разделения K = ", K)    # строка, колонка
B = (np.array([rnd.random() for i in range(N*M)]).reshape(N, M) * 10).astype('int') - 5
print("Исходная матрица B\n", B)

I = np.array_split(B, [0, L])
print("Делим по строкам по L на две части\n", I)

II = np.array_split(I[1], [0, K], axis=1)
print("Делим по столбцам верхнюю часть (I-IV квадранты)\n", II)

III = np.array_split(I[2], [0, K], axis=1)
print("Делим по столбцам нижнюю часть (II-III квадранты)\n", III)
sum_I = np.sum(II[1]) / (L * K)
sum_IV = np.sum(II[2]) / ((L) * (M-K))
sum_II = np.sum(III[1]) / ((N-L) * K)
sum_III = np.sum(III[2]) / ((N-L) * (M-K))
print("Среднее в I квадранте =", sum_I)
print("Среднее во II квадранте =", sum_II)
print("Среднее во III квадранте =", sum_III)
print("Среднее в IV квадранте =", sum_IV)

"""
27. Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
случайными элементами. Все элементы имеют целый тип. Дано целое число
H. Определить, какие строки имеют хотя бы одно такое число, а какие не
имеют.
"""
print("\n\nЗадача №27")
N = 6       # строк
M = 10      # колонок
H = 4       # задано число
print("Строк N =", N, "\nКолонок M =", M, "\nЗадано число H =", H)

B = (np.array([rnd.random() for i in range(N*M)]).reshape(N, M) * 10).astype('int') - 5
print("Исходная матрица B\n", B)

"""
28. Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
случайными элементами. Исключить из матрицы столбец с номером K.
Сомкнуть столбцы матрицы.
"""
print("\n\nЗадача №28")
N = 6    # строк
M = 10    # колонок
print("Строк N = ", N, "\nКолонок M = ", M)

L = 2
K = 4
print("Строка для разделения L = ", L, "\nКолонка для разделения K = ", K)    # колонок
B = (np.array([rnd.random() for i in range(N*M)]).reshape(N, M) * 10).astype('int') - 5
print("Исходная матрица B\n", B)

"""
29. Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
случайными элементами. Добавить к матрице столбец чисел и вставить его
под номером K.
"""
print("\n\nЗадача №29")
N = 6    # строк
M = 10    # колонок
print("Строк N = ", N, "\nКолонок M = ", M)

K = 4
print("Номер колонки, куда будем вставлять, K = ", K)    # колонок
B = (np.array([rnd.random() for i in range(N*M)]).reshape(N, M) * 10).astype('int') - 5
print("Исходная матрица B\n", B)

A = (np.array([rnd.random() for i in range(N)]) * 100).astype("int") - 50
print("Будем вставлять А\n", A)

C = np.insert(B, K, A, axis=1)
print("Результат: матрица C\n", C)


"""
30. Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
случайными элементами. Добавить к элементам каждого столбца такой
новый элемент, чтобы сумма положительных элементов стала бы равна
модулю суммы отрицательных элементов. Результат оформить в виде
матрицы из N + 1 строк и M столбцов.
"""
print("\n\nЗадача №30")
N = 6    # строк
M = 10    # колонок
print("Строк N = ", N, "\nКолонок M = ", M)

B = (np.array([rnd.random() for i in range(N*M)]).reshape(N, M) * 100).astype('int') - 50
print("Исходная матрица B\n", B)

positive_sum = np.zeros(M, dtype=int)
negative_sum = np.zeros(M, dtype=int)

for j in range(M):
    positive_sum[j] = 0
    negative_sum[j] = 0
    for i in range(N):
        if B[i][j] > 0:
            positive_sum[j] += B[i][j]
        else:
            negative_sum[j] += np.abs(B[i][j])

add_row = negative_sum - positive_sum
print("Сумма положительных элементов в колонках:", positive_sum)
print("Сумма абсолютных значений отрицательных элементов в колонках:", negative_sum)
print("Надо добавить строку:", add_row)

C = np.row_stack((B, add_row))
print("Результат новая матрица C\n", C)

"""
31. Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
случайными элементами. Добавить к элементам каждой строки такой новый
элемент, чтобы сумма положительных элементов стала бы равна модулю
суммы отрицательных элементов. Результат оформить в виде матрицы из N
строк и M + 1 столбцов
"""
print("\n\nЗадача №31")
N = 6    # строк
M = 10    # колонок
print("Строк N = ", N, "\nКолонок M = ", M)
B = (np.array([rnd.random() for i in range(N*M)]).reshape(N, M) * 100).astype('int') - 50
print("Исходная матрица B\n", B)

positive_sum = np.zeros(N, dtype=int)
negative_sum = np.zeros(N, dtype=int)

for i in range(N):
    positive_sum[i] = 0
    negative_sum[i] = 0
    for j in range(M):
        if B[i][j] > 0:
            positive_sum[i] += B[i][j]
        else:
            negative_sum[i] += np.abs(B[i][j])

add_col = negative_sum - positive_sum
print("Сумма положительных элементов в строках:", positive_sum)
print("Сумма абсолютных значений отрицательных элементов в строках:", negative_sum)
print("Надо добавить колонку:", add_col)

C = np.column_stack((B, add_col))
print("Результат новая матрица C\n", C)

