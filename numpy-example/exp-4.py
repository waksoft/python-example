import numpy as np
import cv2
from matplotlib import pyplot as plt

I = cv2.imread('susu-2019.jpg')[:, :, ::-1]
I_ = I.reshape(I.shape[0] // 2, 2, I.shape[1] // 2, 2, -1)
Ih = np.hstack((I_[:, 0, :, 0], I_[:, 0, :, 1]))
Iv = np.vstack((I_[:, 0, :, 0], I_[:, 1, :, 0]))
flg = plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
plt.imshow(Ih)
plt.show()
flg.savefig('./output-images/ext-41.jpg')

flg = plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
plt.imshow(Iv)
plt.show()
flg.savefig('./output-images/ext-42.jpg')
