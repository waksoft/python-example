from matplotlib import animation, rc
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
import matplotlib.colors as clr
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

def mandelbrot(pmin, pmax, ppoints, qmin, qmax, qpoints,
               max_iterations=200, infinity_border=10):
    image = np.zeros((ppoints, qpoints))
    p, q = np.mgrid[pmin:pmax:(ppoints*1j), qmin:qmax:(qpoints*1j)]
    c = p + 1j*q
    z = np.zeros_like(c)
    for k in range(max_iterations):
        z = z**2 + c
        mask = (np.abs(z) > infinity_border) & (image == 0)
        image[mask] = k
        z[mask] = np.nan
    return -image.T

rc('animation', html='html5')
# отображать анимацию в виде html5 video

fig = plt.figure(figsize=(10, 10))
max_frames = 200
max_zoom = 300
pmin, pmax, qmin, qmax = -2.5, 1.5, -2, 2

images = []
# кэш картинок

def init():
    return plt.gca()


def animate(i):
    if i > max_frames // 2:
        # фаза zoom out, можно достать картинку из кэша

        plt.imshow(images[max_frames // 2 - i], cmap=cmap)
        return

    p_center, q_center = -0.793191078177363, 0.16093721735804
    zoom = (i / max_frames * 2) ** 3 * max_zoom + 1
    scalefactor = 1 / zoom
    pmin_ = (pmin - p_center) * scalefactor + p_center
    qmin_ = (qmin - q_center) * scalefactor + q_center
    pmax_ = (pmax - p_center) * scalefactor + p_center
    qmax_ = (qmax - q_center) * scalefactor + q_center
    image = mandelbrot(pmin_, pmax_, 500, qmin_, qmax_, 500)
    plt.imshow(image, cmap=cmap)
    images.append(image)
    print(pmin, " ", qmin)
    print(pmax, " ", qmax)

    # добавить картинку в кэш
    return plt.gca()

animation.FuncAnimation(fig, animate, init_func=init, frames=max_frames, interval=50)