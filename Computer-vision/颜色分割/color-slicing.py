import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread('./image/fish.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hsv_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

array = np.array([1, 190, 180])
light_orange = array
dark_orange = np.array([18, 255, 255])

light_white = np.array([0, 0, 220])
dark_white = np.array([170, 40, 260])

light_black = np.array([0, 0, 0])
dark_black = np.array([200, 255, 46])


orange_mask = cv2.inRange(hsv_img, light_orange, dark_orange)
white_mask = cv2.inRange(hsv_img, light_white, dark_white)
black_mask = cv2.inRange(hsv_img, light_black, dark_black)


result_orange = cv2.bitwise_and(img, img, mask=orange_mask)
result_white = cv2.bitwise_and(img, img, mask=white_mask)
result_black = cv2.bitwise_and(img, img, mask=black_mask)
result = result_white + result_orange + result_black
x = result.shape[0]
y = result.shape[1]
for i in range(0, x):
    for j in range(0, y):
        if not (np.any(result[i, j])):
            result[i, j] = (0, 0, 255)

plt.subplot(221)
plt.imshow(orange_mask, cmap="gray")
plt.subplot(222)
plt.imshow(white_mask, cmap='gray')
plt.subplot(223)
plt.imshow(black_mask, cmap='gray')
plt.subplot(224)
plt.imshow(result)
plt.show()
