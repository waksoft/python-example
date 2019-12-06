"""
Имя проекта: Boring-numpy
Номер версии: 1.0
Имя файла: exp-6.py
Автор: 2019 © В.В. Костерин, Челябинск

Дата создания: 06/12/2019
Дата последней модификации: 06/12/2019

Связанные файлы/пакеты: opencv, matplotlib

Описание: загружаем картинку из файла и транспонируем её (поворачиваем на 90)
           всякими разными способаи

#версия Python: 3.6
"""

import cv2
from matplotlib import pyplot as plt

def smooth(I):
    J = I.copy()

    J[1:-1] = (J[1:-1] // 2 + J[:-2] // 4 + J[2:] // 4)
    J[:, 1:-1] = (J[:, 1:-1] // 2 + J[:, :-2] // 4 + J[:, 2:] // 4)

    return J

I_noise = cv2.imread('susu-new-year-noise.jpg')

I_denoise_1 = smooth(I_noise)
I_denoise_2 = smooth(I_denoise_1)
I_denoise_3 = smooth(I_denoise_2)

cv2.imwrite('./output-images/susu-new-year-noise_1.jpg', I_denoise_1)
cv2.imwrite('./output-images/susu-new-year-noise_2.jpg', I_denoise_2)
cv2.imwrite('./output-images/susu-new-year-noise_3.jpg', I_denoise_3)
