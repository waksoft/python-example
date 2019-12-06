"""
Имя проекта: Boring-numpy
Номер версии: 1.0
Имя файла: exp-1.py
Автор: 2019 © В.В. Костерин, Челябинск

Дата создания: 06/12/2019
Дата последней модификации: 06/12/2019

Связанные файлы/пакеты: opencv, matplotlib

Описание: загружаем и показываем картинку из файла

#версия Python: 3.6
"""

import cv2
from matplotlib import pyplot as plt

I = cv2.imread('susu-new-year.jpg')[:, :, ::-1]
flg = plt.figure(num=None, figsize=(15, 15), dpi=80, facecolor='w', edgecolor='k')
plt.imshow(I)
plt.show()

flg.savefig('./output-images/ext-1.jpg')