import cv2
import numpy as np
import matplotlib.pyplot as plt

def homomorphic_filter(src, d0=1, rL=0.2, rH=3, c=4, h=2.0, l=0.5):

    #图像灰度化处理
    gray = src.copy()
    if len(src.shape) > 2:#维度>2
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    #设置数据维度n
    rows = gray.shape[0]
    cols = gray.shape[1]

    #傅里叶变换
    gray_fft = np.fft.fft2(gray) 

    #将零频点移到频谱的中间，就是中间化处理
    gray_fftshift = np.fft.fftshift(gray_fft)

    #生成一个和gray_fftshift一样的全零数据结构
    dst_fftshift = np.zeros_like(gray_fftshift)

    #arange函数用于创建等差数组，分解f(x,y)=i(x,y)r(x,y)
    M, N = np.meshgrid(np.arange(-cols // 2, cols // 2), np.arange(-rows//2, rows//2))#注意，//就是除法

    #使用频率增强函数处理原函数（也就是处理原图像dst_fftshift）
    D = np.sqrt(M ** 2 + N ** 2)#**2是平方
    Z = (rH - rL) * (1 - np.exp(-c * (D ** 2 / d0 ** 2))) + rL
    dst_fftshift = Z * gray_fftshift
    dst_fftshift = (h - l) * dst_fftshift + l

    #傅里叶反变换（之前是正变换，现在该反变换变回去了）
    dst_ifftshift = np.fft.ifftshift(dst_fftshift)
    dst_ifft = np.fft.ifft2(dst_ifftshift)

    #选取元素的实部
    dst = np.real(dst_ifft)

    #dst中，比0小的都会变成0，比0大的都变成255
    #uint8是专门用于存储各种图像的（包括RGB，灰度图像等），范围是从0-255
    dst = np.uint8(np.clip(dst, 0, 255))
    return dst

if __name__ == "__main__":
    img = cv2.imread('./image/HF.jpg',0)
    #将图片执行同态滤波器
    img_new = homomorphic_filter(img)

    plt.subplot(211)
    plt.axis('off')
    plt.title('original image')
    plt.imshow(img, cmap='gray')

    plt.subplot(212)
    plt.axis('off')
    plt.title('result image')
    plt.imshow(img_new, cmap='gray')

    plt.show()



