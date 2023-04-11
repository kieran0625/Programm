# coding=utf-8
from PIL import Image
import numpy as np
import time
import matplotlib.pyplot as plt

def nearest(srcImg, dstH, dstW):
    srcH, srcW, _ = srcImg.shape
    # 将原图像的高度和宽度扩展一个像素
    # 目的是为了防止后面的计算出现数组越界的情况
    srcImg = np.pad(srcImg, ((0,1),(0,1),(0,0)), mode='reflect')
    # 创建目标图像
    dstImg = np.zeros((dstH, dstW, 3), dtype=np.uint8)
    # 遍历目标图像中的每个像素点
    for dstX in range(dstH):
        for dstY in range(dstW):
            # 寻找目标图像上的一个点对应在原图像上的位置 (x, y)
            # 注意这里的x和y不是一个整数
            x = dstX * (srcH / dstH)
            y = dstY * (srcW / dstW)
            # 将x和y进行向下取整，得到原图上对应的像素位置(scrX, srcY)
            scrX = int(x)
            srcY = int(y)
            # 计算目标像素与原图像上整数像素之间的距离
            u = x - scrX
            v = y - srcY
            # 根据距离来判断该选择周围四个像素中哪个像素
            if u > 0.5:
                scrX += 1
            if v > 0.5:
                srcY += 1
            # 选择原图像上距离最近的那个像素作为目标像素的值
            dstImg[dstX, dstY] = srcImg[scrX, srcY]
    return dstImg.astype(np.uint8)


def bilinear(srcImg, dstH, dstW):
    srcH, srcW, _ = srcImg.shape
    # 将原图像的高度和宽度扩展一个像素
    # 目的是为了防止后面的计算出现数组越界的情况
    srcImg = np.pad(srcImg, ((0,1),(0,1),(0,0)), mode='reflect')
    # 创建目标图像
    dstImg = np.zeros((dstH, dstW, 3), dtype=np.uint8)
    # 遍历目标图像中的每个像素点
    for dstX in range(dstH):
        for dstY in range(dstW):
            # 寻找目标图像上的一个点对应在原图像上的位置 (x, y)
            # 注意这里的x和y不是一个整数
            x = dstX * (srcH / dstH)
            y = dstY * (srcW / dstW)
            # 将x和y进行向下取整，得到原图上对应的像素位置(scrX, srcY)
            scrX = int(x)
            srcY = int(y)
            # 计算目标像素与原图像上整数像素之间的距离
            u = x - scrX
            v = y - srcY
            # 计算目标像素值，通过原图像四个整数像素的加权和
            dstImg[dstX, dstY] = (1-u) * (1-v) * srcImg[scrX,   srcY  ] + \
                                 u     * (1-v) * srcImg[scrX+1, srcY  ] + \
                                 (1-u) * v     * srcImg[scrX,   srcY+1] + \
                                 u     * v     * srcImg[scrX+1, srcY+1]
    return dstImg.astype(np.uint8)


if __name__ == '__main__':

    img = np.asarray(Image.open('./image/test.jpg'))
    # 512 x 512

    start = time.time()
    img_n = nearest(img, 800, 600)
    img_b = bilinear(img, 800, 600)

    Image.fromarray(img_n).save('near.png')
    Image.fromarray(img_b).save('bili.png')

