import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号 #有中文出现的情况，需要u'内容'

img = cv2.imread('./image/1-2.png',0)

gray = img.copy()
if len(img.shape) > 2:#维度>2
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

rows = gray.shape[0]
cols = gray.shape[1]
#傅里叶变换
dft = np.fft.fft2(gray)
dft_shift = np.fft.fftshift(dft)
# fft结果是复数，求绝对值结果才是振幅
fimg = np.log(np.abs(dft_shift))

# create a mask first, center square is 1, remaining all zeros
mask = np.zeros((rows, cols), np.uint8)
for i in range(rows):
    for j in range(cols):
        mask[i][j] = 1

mask[int(324):int(337), int(335):int(366)] = 0
mask[int(324):int(337), int(275):int(300)] = 0

# apply mask and inverse DFT
fshift = dft_shift * mask
fimg_new = np.log(np.abs(fshift))

# fftshit()函数的逆函数，它将频谱图像的中心低频部分移动至左上角
f_ishift = np.fft.ifftshift(fshift)
# 将频率域转化回空间域，输出是一个复数，cv2.idft()返回的是一个双通道图像
img_back = np.fft.ifft2(f_ishift)
# idft[:,:,0]求得实部，用idft[:,:,1]求得虚部。
img_back2 = np.abs(img_back)
plt.subplot(2, 2, 1)
plt.title('原始图像')
plt.imshow(img, cmap='gray')
plt.subplot(2, 2, 2)
plt.title('傅里叶频谱')
plt.imshow(fimg, cmap='gray')
plt.subplot(2, 2, 3)
plt.title('处理后傅里叶频谱')
plt.imshow(fimg_new, cmap='gray')
plt.subplot(2, 2, 4)
plt.title('结果图')
plt.imshow(img_back2, cmap='gray')
plt.show()