import cv2
import matplotlib.pyplot as plt
import numpy as np

img_bgr = cv2.imread('./image/fish.jpg',cv2.IMREAD_COLOR)
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
r = img_rgb[:, :, 0]
g = img_rgb[:, :, 1]
b = img_rgb[:, :, 2]
vis = np.zeros(r.shape, dtype='uint8')
orange_range = {'xmin':98, 'ymin':291, 'xmax':123, 'ymax':331}
white_range = {'xmin':114, 'ymin':376, 'xmax':132, 'ymax':395}
black_range = {'xmin':139, 'ymin':337, 'xmax':148, 'ymax':350}
img_orange = img_rgb[orange_range['xmin']:orange_range['xmax'],orange_range['ymin']:orange_range['ymax'],:]
img_white = img_rgb[white_range['xmin']:white_range['xmax'],white_range['ymin']:white_range['ymax'],:]
img_black = img_rgb[black_range['xmin']:black_range['xmax'],black_range['ymin']:black_range['ymax'],:]

orange_u=np.zeros(3)
for i in range(img_orange.shape[2]):
    orange_u[i] = np.mean(img_orange[:, :, i])
orange_d=np.zeros(3)
for i in range(img_orange.shape[2]):
    for j in range(img_orange[:,:,i].shape[0]):
        for k in range(img_orange[:,:,i].shape[1]):
            orange_d[i]=orange_d[i]+(img_orange[j,k,i]-orange_u[i])*(img_orange[j,k,i]-orange_u[i])
    orange_d[i] = np.sqrt(orange_d[i]/img_orange[:,:,i].shape[0]/img_orange[:,:,1].shape[1])

white_u=np.zeros(3)
for i in range(img_white.shape[2]):
    white_u[i] = np.mean(img_white[:,:,i])
white_d=np.zeros(3)
for i in range(img_white.shape[2]):
    for j in range(img_white[:,:,i].shape[0]):
        for k in range(img_white[:,:,i].shape[1]):
            white_d[i]=white_d[i]+(img_white[j,k,i]-white_u[i])*(img_white[j,k,i]-white_u[i])
    white_d[i] = np.sqrt(white_d[i]/img_white[:,:,i].shape[0]/img_white[:,:,1].shape[1])

black_u = np.zeros(3)
for i in range(img_black.shape[2]):
    black_u[i] = np.mean(img_black[:, :, i])
black_d = np.zeros(3)
for i in range(img_black.shape[2]):
    for j in range(img_black[:, :, i].shape[0]):
        for k in range(img_black[:, :, i].shape[1]):
            black_d[i] = black_d[i] + (img_black[j, k, i] - black_u[i]) * (img_black[j, k, i] - black_u[i])
    black_d[i] = np.sqrt(black_d[i] / img_black[:, :, i].shape[0] / img_black[:, :, 1].shape[1])
    
D=10 #比例系数
for i in range(img_rgb.shape[0]):
    for j in range(img_rgb.shape[1]):
        if abs(img_rgb[i,j,0]-orange_u[0])<=D*orange_d[0]:
            if abs(img_rgb[i,j,1]-orange_u[1])<=D*orange_d[1]:
                if abs(img_rgb[i,j,2]-orange_u[2])<=D*orange_d[2]:
                    vis[i,j]=1
        if abs(img_rgb[i,j,0]-white_u[0])<=D*white_d[0]:
            if abs(img_rgb[i,j,1]-white_u[1])<=D*white_d[1]:
                if abs(img_rgb[i,j,2]-white_u[2])<=D*white_d[2]:
                    vis[i,j]=1
        if abs(img_rgb[i,j,0]-black_u[0])<=D*black_d[0]:
            if abs(img_rgb[i,j,1]-black_u[1])<=D*black_d[1]:
                if abs(img_rgb[i,j,2]-black_u[2])<=D*black_d[2]:
                    vis[i,j]=1

img2 = 128*np.ones(img_rgb.shape, dtype='uint8')
for i in range(img_rgb.shape[0]):
    for j in range(img_rgb.shape[1]):
        if vis[i,j]==1:
            img2[i,j,:]=img_rgb[i,j,:]

plt.imshow(img2)
plt.show()
