import numpy as np
import matplotlib.pyplot as plt
# библиотеки

# инициализиация
pmin, pmax, qmin, qmax = -2.5, 1.5, -2, 2
# пусть c = p + iq и p меняется в диапазоне от pmin до pmax,
# а q меняется в диапазоне от qmin до qmax

ppoints, qpoints = 200, 200
# число точек по горизонтали и вертикали

max_iterations = 300
# максимальное количество итераций

infinity_border = 10
# если ушли на это расстояние, считаем, что ушли на бесконечность

image = np.zeros((ppoints, qpoints))
# image — это двумерный массив, в котором будет записана наша картинка
# по умолчанию он заполнен нулями

for ip, p in enumerate(np.linspace(pmin, pmax, ppoints)):
    for iq, q in enumerate(np.linspace(qmin, qmax, qpoints)):
        c = p + 1j * q
        # буквой j обозначается мнимая единица: чтобы Python понимал, что речь
        # идёт о комплексном числе, а не о переменной j, мы пишем 1j

        z = 0
        for k in range(max_iterations):
            z = z ** 2 + c
            # Самая Главная Формула

            if abs(z) > infinity_border:
                # если z достаточно большое, считаем, что последовательость
                # ушла на бесконечность
                # или уйдёт
                # можно доказать, что infinity_border можно взять равным 4

                image[ip, iq] = 1
                # находимся вне M: отметить точку как белую
                break
plt.xticks([])
plt.yticks([])
# выключим метки на осях

plt.imshow(-image.T, cmap='Greys')
# транспонируем картинку, чтобы оси были направлены правильно
# перед image стоит знак минус, чтобы множество Мандельброта рисовалось
# чёрным цветом

plt.show()