import cv2
import matplotlib.pyplot as plt

img_template = cv2.imread('./image/detection/2.jpg')
img_target = cv2.imread('./image/detection/1.png')
img_gray = cv2.cvtColor(img_template, cv2.COLOR_BGR2GRAY)
# 转换为二值图
ret, binary = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
# 获取图像的轮廓参数
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    print(str(i) ,cv2.moments(contours[i]))

#获得模板图片的高宽尺寸
height, width = img_template.shape[:2]
#执行模板匹配，采用的匹配方式cv2.TM_SQDIFF_NORMED
result = cv2.matchTemplate(img_target,img_template,cv2.TM_SQDIFF_NORMED)
#归一化处理
cv2.normalize( result, result, 0, 1, cv2.NORM_MINMAX, -1 )
#寻找矩阵（一维数组当做向量，用Mat定义）中的最大值和最小值的匹配结果及其位置
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
'''
#匹配值转换为字符串
#对于cv2.TM_SQDIFF及cv2.TM_SQDIFF_NORMED方法min_val越趋近与0匹配度越好，匹配位置取min_loc
#对于其他方法max_val越趋近于1匹配度越好，匹配位置取max_loc
'''
strmin_val = str(min_val)
'''
绘制矩形边框，将匹配区域标注出来
#min_loc：矩形定点
#(min_loc[0]+width,min_loc[1]+height)：矩形的宽高
#(0,0,225)：矩形的边框颜色；2：矩形边框宽度
'''
cv2.rectangle(img_target,min_loc,(min_loc[0]+width,min_loc[1]+height),(0,0,255),2)
#显示结果,并将匹配值显示在标题栏上
cv2.namedWindow('result',cv2.WINDOW_NORMAL)
cv2.resizeWindow('result', 400,400)
cv2.imshow('result',img_target)
cv2.waitKey()
cv2.destroyAllWindows()