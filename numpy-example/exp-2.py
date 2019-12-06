"""
Имя проекта: Boring-numpy
Номер версии: 1.0
Имя файла: exp-2.py
Автор: 2019 © В.В. Костерин, Челябинск

Дата создания: 06/12/2019
Дата последней модификации: 06/12/2019

Связанные файлы/пакеты: opencv, matplotlib

Описание: загружаем картинку из файла, в 2 раза уменьшаем размер
          по обеим осям и показываем

#версия Python: 3.6
"""

import cv2
from matplotlib import pyplot as plt

I = cv2.imread('susu-new-year.jpg')[:, :, ::-1]
plt.figure(num=None, figsize=(15, 15), dpi=80, facecolor='w', edgecolor='k')
plt.imshow(I)
plt.show()

I_ = I.reshape(I.shape[0] // 2, 2, I.shape[1] // 2, 2, -1)
print(I_.shape)
flg = plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
plt.imshow(I_[:, 0, :, 0])
plt.show()

flg.savefig('./output-images/ext-2.jpg')