import cv2
import numpy as np
import matplotlib.pyplot as plt
def adjust_gamma(image, gamma=1.0):
    # 建立查找表，将像素值[0，255]映射到调整后的伽玛值
    # 遍历[0，255]范围内的所有像素值来构建查找表，然后再提高到反伽马的幂-然后将该值存储在表格中
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")

    # 使用查找表应用伽玛校正
    return cv2.LUT(image, table)

# 读取珍珠图像
img = cv2.imread('./image/2-1.jpg')
Gau = cv2.GaussianBlur(img,(3,3),1)
# 转换为灰度图像
gray_image = cv2.cvtColor(Gau, cv2.COLOR_BGR2GRAY)

gamma_img = adjust_gamma(gray_image, 0.2)
cv2.imshow('gamma', gamma_img)
# 绘制灰度图
hist1 = cv2.calcHist([img],[0],None,[256],[0,256])
plt.figure()#新建一个图像
plt.title("Grayscale Histogram")#图像的标题
plt.xlabel("Bins")#X轴标签
plt.ylabel("# of Pixels")#Y轴标签
plt.plot(hist1)#画图
plt.xlim([0,256])#设置x坐标轴范围
#对直方图进行均衡化

equ = cv2.equalizeHist(gamma_img)
cv2.imshow('equ',equ)
#绘制灰度均衡化以后的直方图
hist2 = cv2.calcHist([equ],[0],None,[256],[0,256])
plt.figure()#新建一个图像
plt.title("Grayscale Histogram")#图像的标题
plt.xlabel("Bins")#X轴标签
plt.ylabel("# of Pixels")#Y轴标签
plt.plot(hist2)#画图
plt.xlim([0,256])#设置x坐标轴范围
#对图像进行二值化处理

ret,img1 = cv2.threshold(equ,200,255,cv2.THRESH_BINARY)
# 应用Canny边缘检测器
edges = cv2.Canny(equ, 100, 200)
cv2.imshow('Canny', edges)

# 检测珍珠的轮廓
# contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
circles1 = cv2.HoughCircles(equ,cv2.HOUGH_GRADIENT,1,55,param1=100,param2=25,minRadius=20,maxRadius=60)
print(circles1)
circles = circles1[0,:,:]#提取为二维
print(circles)
circles = np.uint16(np.around(circles))#四舍五入，取整
for i in circles[:]:
    cv2.circle(img,(i[0],i[1]),i[2],(255,0,0),2)#画圆
    cv2.circle(img,(i[0],i[1]),2,(255,0,255),5)#画圆心
    # # 绘制珍珠轮廓
    # cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

# 显示结果
cv2.imshow('Pearl Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
plt.show()