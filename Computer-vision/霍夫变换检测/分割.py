import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("./image/2-2.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)
edged = cv2.Canny(blurred, 30, 150, apertureSize=3)
circles1 = cv2.HoughCircles(edged, cv2.HOUGH_GRADIENT, 1,
                            100, param1=100, param2=30, minRadius=1, maxRadius=100)

circles = np.uint16(np.around(circles1))

circles_count = 0
for i in circles[0, :]:
    cv2.circle(image, (i[0], i[1]), i[2], (255, 0, 0), 2)
    circles_count = 1+circles_count
    cv2.circle(image, (i[0], i[1]), 2, (0, 0, 255), 1)
print("圆形个数:", circles_count)
coins = image.copy()
plt.subplot(121)
plt.title('Division')
plt.imshow(edged)
plt.subplot(122)
plt.title('Testing')
plt.imshow(coins)
plt.show()


