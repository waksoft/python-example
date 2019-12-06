import cv2
from matplotlib import pyplot as plt

def smooth(I):
    J = I.copy()

    J[1:-1] = (J[1:-1] // 2 + J[:-2] // 4 + J[2:] // 4)
    J[:, 1:-1] = (J[:, 1:-1] // 2 + J[:, :-2] // 4 + J[:, 2:] // 4)

    return J

I_noise = cv2.imread('susu-noise.jpg')

I_denoise_1 = smooth(I_noise)
I_denoise_2 = smooth(I_denoise_1)
I_denoise_3 = smooth(I_denoise_2)

cv2.imwrite('./output-images/susu-noise.jpg', I_noise)
cv2.imwrite('./output-images/susu-noise_1.jpg', I_denoise_1)
cv2.imwrite('./output-images/susu-noise_2.jpg', I_denoise_2)
cv2.imwrite('./output-images/susu-noise_3.jpg', I_denoise_3)
