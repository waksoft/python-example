"""
Имя проекта: Boring-numpy
Номер версии: 1.0
Имя файла: exp-7.py
Автор: 2019 © В.В. Костерин, Челябинск

Дата создания: 06/12/2019
Дата последней модификации: 06/12/2019

Связанные файлы/пакеты: opencv, matplotlib

Описание: как оптимизирован показ ядра при фильтрайии

#версия Python: 3.6
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

def smooth(I):
    J = I.copy()

    J[1:-1] = (J[1:-1] // 2 + J[:-2] // 4 + J[2:] // 4)
    J[:, 1:-1] = (J[:, 1:-1] // 2 + J[:, :-2] // 4 + J[:, 2:] // 4)

    return J

M = np.zeros((11, 11))

M[5, 5] = 255
M1 = smooth(M)
M2 = smooth(M1)
M3 = smooth(M2)

flg = plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
plt.subplot(1, 3, 1)
plt.imshow(M1)

plt.subplot(1, 3, 2)
plt.imshow(M2)

plt.subplot(1, 3, 3)
plt.imshow(M3)

plt.show()
flg.savefig('./output-images/ext-7.jpg')