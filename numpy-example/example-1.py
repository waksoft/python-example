#имя проекта: numpy-example
#имя файла: example_1.py
#номер версии: 1.011
#автор и его учебная группа: Е. Волков, ЭУ-142
#дата создания: 20.03.2019
# дата последней модификации: 25.03.2019
#связанные файлы: пакеты numpy, matplotlib
# описание: построение графика сигма-функции
#версия Python: 3.6

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)

def sigmoid(alpha):
    return 1 / ( 1 + np.exp(- alpha * x))

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi))
plt.plot(x, sigmoid(0.5), 'ro-')
plt.plot(x, sigmoid(1.0), 'go-')
plt.plot(x, sigmoid(2.0), 'bo-')
plt.legend(['A = 0.5', 'A = 1.0', 'A = 2.0'], loc = 'upper left')

plt.show()

fig.savefig('sigmoid.png')