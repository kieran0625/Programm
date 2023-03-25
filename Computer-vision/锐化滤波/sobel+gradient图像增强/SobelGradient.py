import numpy as np
import cv2

# Laplace算子
# 常用的Laplace算子模板  [[0,1,0],[1,-4,1],[0,1,0]]   [[1,1,1],[1,-8,1],[1,1,1]]
def Laplace(img):
    r = img.shape[0]
    c = img.shape[1]
    laplace_image = np.zeros((r, c))
    # L_sunnzi = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
    L_sunnzi = np.array([[1,1,1],[1,-8,1],[1,1,1]])
    for i in range(r-2):
        for j in range(c-2):
            laplace_image[i+1, j+1] = abs(np.sum(img[i:i+3, j:j+3] * L_sunnzi))
    return np.uint8(laplace_image)

# 使用sobel算子进行图像细节增强
def Sobel(img):
    r = img.shape[0]
    c = img.shape[1]
    sobel_image = np.zeros((r, c))
    sobel_imageX = np.zeros(img.shape)
    sobel_imageY = np.zeros(img.shape)
    s_suanziX = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])      # X方向
    s_suanziY = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])      # Y方向
    for i in range(r-2):
        for j in range(c-2):
            sobel_imageX[i+1, j+1] = abs(np.sum(img[i:i+3, j:j+3] * s_suanziX))
            sobel_imageY[i+1, j+1] = abs(np.sum(img[i:i+3, j:j+3] * s_suanziY))
            sobel_image[i+1, j+1] = (sobel_imageX[i+1, j+1]*sobel_imageX[i+1,j+1] + sobel_imageY[i+1, j+1]*sobel_imageY[i+1,j+1])**0.5
    # return np.uint8(laplace_imageX)
    # return np.uint8(laplace_imageY)
    return np.uint8(sobel_image)  # 无方向算子处理的图像

def Combination(img,sobel_image,laplace_image):
    r = img.shape[0]
    c = img.shape[1]
    com_image = np.zeros((r, c))
    for i in range(0, r):
        for j in range(0, c):
            com_image[i][j] = img[i][j] - sobel_image[i][j] - laplace_image[i][j]
    return np.uint8(com_image)  # 无方向算子处理的图像

if __name__ == '__main__':
    img = cv2.imread('./image/image_hance/body_x_ray.jpg',0)
    cv2.imshow('image', img)
    out_laplace = Laplace(img)
    cv2.imshow('out_laplace',out_laplace)
    out_sobel = Sobel(img)
    cv2.imshow('out_sobel',out_sobel)
    out_all = Combination(img,out_sobel,out_laplace)
    cv2.imshow('out_all',out_all)
    cv2.waitKey(0)
    cv2.destroyAllWindows()