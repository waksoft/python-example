"""
Имя проекта: Boring-numpy
Номер версии: 1.0
Имя файла: exp-5.py
Автор: 2019 © В.В. Костерин, Челябинск

Дата создания: 06/12/2019
Дата последней модификации: 06/12/2019

Связанные файлы/пакеты: numpy, opencv, matplotlib

Описание: загружаем картинку из файла и транспонируем её (поворачиваем на 90)
           всякими разными способаи

#версия Python: 3.6
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

I0 = cv2.imread('susu-new-year.jpg')[:, :, ::-1]     # загрузили большое изображение
I1 = I0.reshape(I0.shape[0] // 2, 2, I0.shape[1] // 2, 2, -1)[:, 0, :, 0]  # уменьшили вдвое по каждому измерению
I2 = np.repeat(I1, 2)  # склонировали данные
I3 = I2.reshape(I1.shape[0], I1.shape[1], I1.shape[2], -1)
I4 = np.transpose(I3, (0, 3, 1, 2)) # поменяли порядок осей
I5 = I4.reshape(-1, I1.shape[1], I1.shape[2]) # объединили оси

print('I0', I0.shape)
print('I1', I1.shape)
print('I2', I2.shape)
print('I3', I3.shape)
print('I4', I4.shape)
print('I5', I5.shape)

flg = plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
plt.imshow(I5)
plt.show()
flg.savefig('./output-images/ext-5.jpg')

