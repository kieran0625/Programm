import cv2
import skimage
import numpy as np
import matplotlib.pyplot as plt
from skimage import morphology,exposure
from skimage.io import imread

img = cv2.imread('./image/image_hance/32.jpg')
src = img.copy()
src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY) # 转为灰度图
con = exposure.adjust_sigmoid(src,0.4)

x_gray = cv2.Sobel(src,cv2.CV_32F,1,0)
y_gray = cv2.Sobel(src,cv2.CV_32F,0,1)
x_gray = cv2.convertScaleAbs(x_gray)
y_gray = cv2.convertScaleAbs(y_gray)
dst = cv2.add(x_gray,y_gray,dtype=cv2.CV_16S)
dst = cv2.convertScaleAbs(dst)
cv2.imshow('dst',dst)

# 对梯度做二值处理，选取一个阈值，大于阈值的设为255，小于阈值的设为0
tmp = dst.copy()
thres = 100
tmp[tmp>thres]=255
tmp[tmp<=thres]=0
cv2.imshow('enhancement',tmp)

labels = ((morphology.closing(tmp, morphology.disk(7))>0)*255).astype(np.uint8)
num_labels,labels,stats,centers = cv2.connectedComponentsWithStats(labels, connectivity=4,ltype=cv2.CV_32S)
for t in range(1, num_labels, 1):
    x, y, w, h, area = stats[t]
    if area>80:
        index = np.where(labels==t)
        labels[index[0], index[1]] = 0
# 提取斑点
mask = (labels>0).astype(np.uint8)*255
cv2.imshow('bandian', mask)
mask_new = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
print(img.shape, mask_new.shape)

result = cv2.bitwise_and(img, mask_new)
cv2.imshow('extractSpeckleAreas',result)



'''
# 参数说明：
num_labels： 代表连通域的数量，包含背景
labels ： 记录img中每个位置对应的label
stats： 每个连通域的外接矩形和面积
centers : 连通域的质心坐标
x, y, w, h, area = stats[t]
centers : 连通域的质心坐标
'''
cv2.waitKey(0)
cv2.destroyAllWindows()