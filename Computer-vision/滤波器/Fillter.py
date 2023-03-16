'''
time:2023/3/14/23:47
图像中值滤波与均值滤波处理：
    (1)加载图片
    (2)中值滤波:中心像素为邻近的3x3区域内的所有像素值的中值(中位数)
    (3)均值滤波:中心像素为临近3x3区域内的所有像素的平均值
    note:均值滤波边缘像素有  1.补0;  2.复制。
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt


def median_filter(image, kernel=3):
    height, width, channel = image.shape
    result = image.copy()
    # 因为卷积核是以左上角为定位，所以遍历时最后要停到height-2处
    for h in range(1, height-2):
        for w in range(1, width-2):
            for c in range(channel):
                result[h, w, c] = np.median(result[h:h+kernel, w:w+kernel, c])
    return result


def mean_filter(img, kernel=3):

    # 均值滤波
    height, width, channel = img.shape
    # 零填充
    pad = kernel//2
    result = np.zeros((height + 2*pad, width + 2 *
                      pad, channel), dtype=np.float16)
    result[pad:pad+height, pad:pad+width] = img.copy().astype(np.float16)
    # 卷积的过程
    tmp = result.copy()
    for h in range(height):
        for w in range(width):
            for c in range(channel):
                result[pad+h, pad+w,
                       c] = np.mean(tmp[h:h+kernel, w:w+kernel, c])
    result = result[pad:pad+height, pad:pad+width].astype(np.uint8)
    return result


if __name__ == "__main__":

    img = cv2.imread(r"./image/image_salt_pepper2.jpg")
    cv2.imshow("original", img)
    MedianFilter_img = median_filter(img)
    MeanFilter_img = mean_filter(img)
    cv2.imshow("MedianFilter_img", MedianFilter_img)
    cv2.imshow("MeanFillter_img", MeanFilter_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
