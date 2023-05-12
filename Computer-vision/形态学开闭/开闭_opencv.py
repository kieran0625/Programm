import cv2
import numpy as np
import matplotlib.pyplot as plt

ori = cv2.imread('./image/mono.jpg')

k = np.ones((15, 15), np.uint8)

#opencv调库
dilation = cv2.dilate(ori,k)
erosion = cv2.erode(ori,k)
opening = cv2.morphologyEx(ori, cv2.MORPH_OPEN, k)
closing = cv2.morphologyEx(ori, cv2.MORPH_CLOSE, k)

plt.subplot(231)
plt.title('Original')
plt.imshow(ori)
plt.subplot(232)
plt.title('dilation')
plt.imshow(dilation)
plt.subplot(233)
plt.title('erosion')
plt.imshow(erosion)
plt.subplot(234)
plt.title('opening')
plt.imshow(opening)
plt.subplot(235)
plt.title('closing')
plt.imshow(closing)
plt.show()

