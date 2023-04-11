# -*- coding: utf-8 -*-
import cv2
import numpy as np

#利用opencv读入图片
ori_img = cv2.imread('./image/image1.bmp',cv2.IMREAD_COLOR)
#opencv库的颜色空间转换结果
hsi_img = cv2.cvtColor(ori_img,cv2.COLOR_BGR2HSV)
h, s, i = cv2.split(cv2.cvtColor(ori_img, cv2.COLOR_BGR2HSV))

'''
hsi_img[:,:,0] #Hue
hsi_img[:,:,1] #saturation
hsi_img[:,:,2] #idensity
'''

# hsi_img[:,:,0] = cv2.blur(hsi_img[:,:,0], (25, 25))
# hsi_img[:,:,1] = cv2.blur(hsi_img[:,:,1], (25, 25))
hsi_img[:,:,2] = cv2.blur(hsi_img[:,:,2], (25, 25))
rgb_img = cv2.cvtColor(hsi_img,cv2.COLOR_HSV2BGR)

# cv2.imshow('hsi',hsi_img)
# cv2.imshow('h',h)
# cv2.imshow('s',s)
# cv2.imshow('i',i)
cv2.imshow('Process Saturation',rgb_img)
cv2.waitKey()
