import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./image/star.png')

msf1 = cv2.pyrMeanShiftFiltering(img, 10, 70)
msf2 = cv2.pyrMeanShiftFiltering(img, 50, 10)
msf3 = cv2.pyrMeanShiftFiltering(img, 60, 70)

plt.subplot(221)
plt.title('Original')
plt.imshow(img)
plt.subplot(222)
plt.title('10,70')
plt.imshow(msf1)
plt.subplot(223)
plt.title('70,10')
plt.imshow(msf2)
plt.subplot(224)
plt.title('60,70')
plt.imshow(msf3)
plt.show()
