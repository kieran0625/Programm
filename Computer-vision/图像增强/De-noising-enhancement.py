'''
time:2023/3/15/9.23
高斯滤波实现去噪增强：
(1)图像文件中包含20个图片,因此采取路径提取,自动实现对图像的高斯滤波
(2)实现的0填充,计算高斯滤波的卷积核
(3)保存到目标文件夹
'''

import cv2
import numpy as np
import os

# Gaussian filter


def gaussian_filter(img, K_size=3, sigma=1.3):
    if len(img.shape) == 3:
        height, width, channel = img.shape
    else:
        img = np.expand_dims(img, axis=-1)
        height, width, channel = img.shape

    # Zero padding
    pad = K_size // 2
    out = np.zeros((height + pad * 2, width + pad *
                   2, channel), dtype=np.float32)
    out[pad: pad + height, pad: pad + width] = img.copy().astype(np.float32)

    # prepare Kernel
    K = np.zeros((K_size, K_size), dtype=np.float32)
    for x in range(-pad, -pad + K_size):
        for y in range(-pad, -pad + K_size):
            K[y + pad, x +
                pad] = np.exp(-(x ** 2 + y ** 2) / (2 * (sigma ** 2)))
    K /= (2 * np.pi * sigma * sigma)
    K /= K.sum()

    tmp = out.copy()
    # filtering
    for h in range(height):
        for w in range(width):
            for c in range(channel):
                out[pad + h, pad + w,
                    c] = np.sum(K * tmp[h: h + K_size, w: w + K_size, c])

    out = np.clip(out, 0, 255)
    out = out[pad: pad + height, pad: pad + width].astype(np.uint8)
    return out


if __name__ == "__main__":

    data_base_dir = r'./image/noise'  # 输入文件夹的路径
    outfile_dir = r'./image/noise/result'  # 输出文件夹的路径

    list = os.listdir(data_base_dir)
    list.sort()
    list2 = os.listdir(outfile_dir)
    list2.sort()
    for file in list:  # 遍历目标文件夹图片
        read_img_name = data_base_dir + '/' + file.strip()  # 取图片完整路径
        # 灰度图读取,用于计算gamma值
        img = cv2.imread(read_img_name, cv2.IMREAD_GRAYSCALE)
        image_gaussian = gaussian_filter(img, K_size=3, sigma=2)  # gamma变换
        out_img_name = outfile_dir + '/' + file.strip()
        cv2.imwrite(out_img_name, image_gaussian)
        print("The photo which is processed is {}".format(file))
    '''
    给得到的图像进行加权平均优化
    img1 = cv2.imread("./image/noise/result/image_noise1.jpg", cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread("./image/noise/result/image_noise2.jpg", cv2.IMREAD_GRAYSCALE)
    img3 = cv2.imread("./image/noise/result/image_noise3.jpg", cv2.IMREAD_GRAYSCALE)
    img4 = cv2.imread("./image/noise/result/image_noise4.jpg", cv2.IMREAD_GRAYSCALE)
    img5 = cv2.imread("./image/noise/result/image_noise5.jpg", cv2.IMREAD_GRAYSCALE)
    img6 = cv2.imread("./image/noise/result/image_noise6.jpg", cv2.IMREAD_GRAYSCALE)
    img7 = cv2.imread("./image/noise/result/image_noise7.jpg", cv2.IMREAD_GRAYSCALE)
    img8 = cv2.imread("./image/noise/result/image_noise8.jpg", cv2.IMREAD_GRAYSCALE)
    img9 = cv2.imread("./image/noise/result/image_noise9.jpg", cv2.IMREAD_GRAYSCALE)
    img10 = cv2.imread("./image/noise/result/image_noise10.jpg", cv2.IMREAD_GRAYSCALE)
    img11 = cv2.imread("./image/noise/result/image_noise11.jpg", cv2.IMREAD_GRAYSCALE)
    img12 = cv2.imread("./image/noise/result/image_noise12.jpg", cv2.IMREAD_GRAYSCALE)
    img13 = cv2.imread("./image/noise/result/image_noise13.jpg", cv2.IMREAD_GRAYSCALE)
    img14 = cv2.imread("./image/noise/result/image_noise14.jpg", cv2.IMREAD_GRAYSCALE)
    img15 = cv2.imread("./image/noise/result/image_noise15.jpg", cv2.IMREAD_GRAYSCALE)
    img16 = cv2.imread("./image/noise/result/image_noise16.jpg", cv2.IMREAD_GRAYSCALE)
    img17 = cv2.imread("./image/noise/result/image_noise17.jpg", cv2.IMREAD_GRAYSCALE)
    img18 = cv2.imread("./image/noise/result/image_noise18.jpg", cv2.IMREAD_GRAYSCALE)
    img19 = cv2.imread("./image/noise/result/image_noise19.jpg", cv2.IMREAD_GRAYSCALE)
    img20 = cv2.imread("./image/noise/result/image_noise20.jpg", cv2.IMREAD_GRAYSCALE)

    img1 = img1.astype(np.float32)
    img2 = img2.astype(np.float32)
    img3 = img3.astype(np.float32)
    img4 =img4.astype(np.float32)
    img5 =img5.astype(np.float32)
    img6 =img6.astype(np.float32)
    img7=img7.astype(np.float32)
    img8=img8.astype(np.float32)
    img9 =img9.astype(np.float32)
    img10=img10.astype(np.float32)
    img11 =img11.astype(np.float32)
    img12=img12.astype(np.float32)
    img13=img13.astype(np.float32)
    img14 =img14.astype(np.float32)
    img15=img15.astype(np.float32)
    img16=img16.astype(np.float32)
    img17=img17.astype(np.float32)
    img18 =img18.astype(np.float32)
    img19 =img19.astype(np.float32)
    img20 =img20.astype(np.float32)
    img = (img1 +img2 +img3 +img4+ img5 +img6+img7 +img8+img9 +img10+
           img11+img12 +img13 +img14+img15+img16+img17 +img18+img19+img20)/20
    img =img.astype(np.uint8)
    cv2.imshow("img",img)
    cv2.imwrite("./image/noise/result/img.jpg",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''
