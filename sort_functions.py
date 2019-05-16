# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

## ---(Sun Jul 29 17:49:50 2018)-

def select(arr, dim):
    # метод простого выбора Select
    # в переменной k хранится индекс элемента, подлежащего обмену (двигаемся слева на право)
    k = 0
    alg_count = [0, 0]

    # alg_count[0] = 0       счетчик перестановок
    # alg_count[1] = 0       счетчик сравнений

    for k in range(0, dim - 1):  # -1, т.к. последний элемент обменивать уже не надо
        m = k  # в m хранится минимальное значение
        i = k + 1  # откуда начинать поиск минимума (элемент следующий за k)
        for i in range(i, dim):
            alg_count[0] += 1
            if arr[i] < arr[m]:
                m = i
        if k != m:
            t = arr[k]
            arr[k] = arr[m]
            arr[m] = t
            alg_count[1] += 1
    #        k += 1 #переходим к следующему значению для обмена
    return alg_count


# метод простой вставки Insert
def insert(arr, dim):
    alg_count = [0, 0]

    # alg_count[0] = 0       счетчик перестановок
    # alg_count[1] = 0       счетчик сравнений

    for i in range(1, dim):  # Основной цикл со 2-го элемента право
        temp = arr[i]  # Запомним элемент для сравнения
        j = i - 1
        while j >= 0:  # Ищем влево ближайший меньший
            alg_count[0] += 1  # Считаем операции сравнения
            if arr[j] > temp:
                alg_count[1] += 1  # Считаем операции перестановки
                arr[j + 1] = arr[j]  # Сдвигаем элемент влево, а на его место ставим наименьший
                arr[j] = temp
            j -= 1
    return alg_count


# метод пузырька Bubble
def bubble(arr, dim):
    n = 1
    alg_count = [0, 0]

    # alg_count[0] = 0       счетчик перестановок
    # alg_count[1] = 0       счетчик сравнений

    while n < dim:
        for i in range(dim - n):
            alg_count[0] += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                alg_count[1] += 1
        n += 1
    return alg_count
