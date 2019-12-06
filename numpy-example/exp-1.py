import cv2

from matplotlib import pyplot as plt

I = cv2.imread('susu-2019.jpg')[:, :, ::-1]
flg = plt.figure(num=None, figsize=(15, 15), dpi=80, facecolor='w', edgecolor='k')
plt.imshow(I)
plt.show()

flg.savefig('./output-images/ext-1.jpg')