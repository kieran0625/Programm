import cv2
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

target= cv2.imread('./image/detection/1.png',cv2.IMREAD_GRAYSCALE)
template = cv2.imread('./image/detection/2.jpg',cv2.IMREAD_GRAYSCALE)


# 构造生成器
orb = cv2.ORB_create()
# 检测图片
kp_tar, des_tar = orb.detectAndCompute(target, None)
kp_temp, des_temp = orb.detectAndCompute(template, None)

print("模板的关键点数目："+str(len(kp_temp)))
print("目标的关键点数目："+str(len(kp_tar)))

# 绘出关键点
img_temp=cv2.drawKeypoints(template,kp_temp,None,(255,0,255))
img_tar=cv2.drawKeypoints(target,kp_tar,None,(255,0,255))
# plt.figure(figsize=(10,10))
# plt.title('sift检测特征点',fontsize=20)
# plt.axis('off')
# plt.imshow(img_tar)
# plt.show()

# 获得一个暴力匹配器的对象
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)
# 利用匹配器 匹配两个描述符的相近程度


matches = bf.knnMatch(des_tar, des_temp, k=2)
print(len(matches))
matchesMask = [[0, 0] for i in range(len(matches))]
for i, (m1, m2) in enumerate(matches):
    if m1.distance < 0.9 * m2.distance:# 两个特征向量之间的欧氏距离，越小表明匹配度越高。
        matchesMask[i] = [1, 0]
        pt1 = kp_tar[m1.queryIdx].pt  # trainIdx    是匹配之后所对应关键点的序号，第一个载入图片的匹配关键点序号
        pt2 = kp_temp[m1.trainIdx].pt  # queryIdx  是匹配之后所对应关键点的序号，第二个载入图片的匹配关键点序号
        # print(kpts1)
        print(i, pt1, pt2)
        if i % 5 ==0:
            cv2.circle(target, (int(pt1[0]),int(pt1[1])), 5, (255,0,255), -1)
            cv2.circle(template, (int(pt2[0]),int(pt2[1])), 5, (255,0,255), -1)

good = []
for m, n in matches:
    if m.distance < 0.9 * n.distance:
        good.append(m)
# matches = sorted(matches, key=lambda x: x.distance)
# print(len(matches))

# 画出匹配项
img_result = cv2.drawMatches(target, kp_tar, template, kp_temp, good[: 50], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
plt.figure(figsize=(10,10))
plt.title('KNN最近邻算法',fontsize=12,color='r')
plt.imshow(img_result)
plt.axis('off')
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()

