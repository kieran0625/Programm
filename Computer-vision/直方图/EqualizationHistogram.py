'''
time: 2023/3/14/23:14
直方图均衡化，增强图片对比度
步骤：
    (1)以灰度图形式加载图片
    (2)计算原图直方图
    (3)计算各像素的概率密度分布，然后乘总数即可
    (4)计算均衡化后得到直方图
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt


def Origin_histogram(img):
    # 建立原始图像各灰度级的灰度值与像素个数对应表
    histogram = {}
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            k = img[i][j]
            if k in histogram:
                histogram[k] += 1
            else:
                histogram[k] = 1

    sorted_histogram = {}  # 建立排好序的映射表
    sorted_list = sorted(histogram)  # 根据灰度值进行从低至高的排序

    for j in range(len(sorted_list)):
        sorted_histogram[sorted_list[j]] = histogram[sorted_list[j]]

    return sorted_histogram


def equalization_histogram(histogram, img):
    intensity = {}  # 建立概率分布映射表

    for i in histogram.keys():
        intensity[i] = histogram[i] / (img.shape[0] * img.shape[1])  # 求取概率

    tmp = 0
    for m in intensity.keys():
        tmp += intensity[m]  # 每次都需要求和
        intensity[m] = max(histogram) * tmp  # 因为从0开始，所以此处就是L-1

    new_img = np.zeros(shape=(img.shape[0], img.shape[1]), dtype=np.uint8)

    for k in range(img.shape[0]):
        for l in range(img.shape[1]):
            new_img[k][l] = intensity[img[k][l]]

    return new_img


def GrayHist(img):
    # 计算灰度直方图
    height, width = img.shape[:2]
    grayHist = np.zeros([256], dtype=np.uint64)
    for i in range(height):
        for j in range(width):
            grayHist[img[i][j]] += 1
    return grayHist


if __name__ == '__main__':
    # 读取原始图像
    img = cv2.imread('./image/2.jpg', cv2.IMREAD_GRAYSCALE)
    # img = cv2.cvtColor(image,cv2.COLOR_BGR2RGB) # TODO:需要更改图片类型为RGB，但是修改后会报错！
    # 计算原图灰度直方图
    origin_histogram = Origin_histogram(img)
    # 直方图均衡化
    new_img = equalization_histogram(origin_histogram, img)

    origin_grayHist = GrayHist(img)
    equaliza_grayHist = GrayHist(new_img)
    x = np.arange(256)
    # 绘制灰度直方图
    plt.figure()
    plt.subplot(2, 2, 1)
    plt.plot(x, origin_grayHist)
    plt.subplot(2, 2, 2)
    plt.plot(x, equaliza_grayHist)
    plt.subplot(2, 2, 3)
    plt.imshow(img)
    plt.subplot(2, 2, 4)
    plt.imshow(new_img)
    plt.show()
