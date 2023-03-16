import numpy as np
import cv2


def adjust_gamma(image, gamma=1.0):
    # 建立查找表，将像素值[0，255]映射到调整后的伽玛值
    # 遍历[0，255]范围内的所有像素值来构建查找表，然后再提高到反伽马的幂-然后将该值存储在表格中
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")

    # 使用查找表应用伽玛校正
    return cv2.LUT(image, table)


if __name__ == "__main__":
    # 加载原始图像
    img = cv2.imread("./image/1.jpg", 0)
    cv2.imshow("original", img)
    img1 = adjust_gamma(img, 0.7)
    img2 = adjust_gamma(img, 1.5)
    cv2.imshow("gamma=0.7", img1)
    cv2.imshow("gamma=1.5", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
