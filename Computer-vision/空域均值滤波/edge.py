'''
边缘效应与滤波
time:2023/3/10/10.10 by Jxw
reasons:当一个n*n的方形卷积核,其中心距离图像边缘为(n-1)/2个像素时,该掩模至少有一条边与图像轮廓相重合，
当掩模的中心继续向图像边缘靠近，那么掩模的行或列就会处于图像平面之外。
通常处理方法为：
    (1) 完全填充 0值
    (2) 边界外的矩阵取镜像反射 'symmetric'参数
    (3) 边界外的矩阵取最邻近的边界值 'replicate'参数
    (4) 边界外的矩阵取周期性的重复值 'circular'参
'''

import cv2
import numpy as np
import torch.nn as nn
import matplotlib.pyplot as plt

img = cv2.imread(r"./image/f.bmp")
img_zero = cv2.copyMakeBorder(img, 10,10,10,10, cv2.BORDER_CONSTANT,value=0)
img_reflect = cv2.copyMakeBorder(img,10,10,10,10, cv2.BORDER_REFLECT)
img_copy = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REPLICATE)

img_zero_blur = cv2.blur(img_zero, (10, 10))
img_reflect_blur = cv2.blur(img_reflect, (10, 10))
img_copy_blur = cv2.blur(img_copy, (10, 10))

plt.figure()
plt.rcParams['font.sans-serif'] = ['SimHei']
ax1=plt.subplot(2,2,1)
ax1.axis('off')
plt.imshow(img)
plt.title("原图")
ax2=plt.subplot(2,2,2)
ax2.axis('off')
plt.imshow(img_zero_blur)
plt.title('零填充')
ax3=plt.subplot(2,2,3)
ax3.axis('off')
plt.title('镜像填充')
plt.imshow(img_reflect_blur)
ax4=plt.subplot(2,2,4)
ax4.axis('off')
plt.title('重复填充')
plt.imshow(img_copy_blur)
plt.show()