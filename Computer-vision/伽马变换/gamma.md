# 一、算法原理

Gamma变换是对输入图像灰度值进行的非线性操作，使输出图像灰度值与输入图像灰度值呈指数关系：
$$
s = c · r^\gamma
$$
Gamma变换就是用来图像增强，其提升了暗部细节，简单来说就是通过非线性变换，让图像从暴光强度的线性响应变得更接近人眼感受的响应，即将漂白（相机曝光）或过暗（曝光不足）的图片，进行矫正。

经过Gamma变换后的输入和输出图像灰度值关系如图1所示：横坐标是输入灰度值，纵坐标是输出灰度值，蓝色曲线是gamma值小于1时的输入输出关系，红色曲线是gamma值大于1时的输入输出关系。可以观察到，当gamma值小于1时(蓝色曲线)，图像的整体亮度值得到提升，同时低灰度处的对比度得到增加，更利于分辩低灰度值时的图像细节。

![](https://imgconvert.csdnimg.cn/aHR0cHM6Ly93d3cuemRhaW90LmNvbS8lRTglQUUlQTElRTclQUUlOTclRTYlOUMlQkElRTglQTclODYlRTglQTclODkvR2FtbWElRTclOUYlQUIlRTYlQUQlQTMvMTM1NzAyOTgzMV81OTA0LnBuZw)

**<font size=5>总结即为：</font>**

1. gamma>1, 较亮的区域灰度被拉伸，较暗的区域灰度被压缩的更暗，图像整体变暗；
2. gamma<1, 较亮的区域灰度被压缩，较暗的区域灰度被拉伸的较亮，图像整体变亮；

> 灰度值为0时为黑色，255为白色。

# 二、关键代码

```python
def adjust_gamma(image, gamma=1.0):
    # 建立查找表，将像素值[0，255]映射到调整后的伽玛值
    # 遍历[0，255]范围内的所有像素值来构建查找表，然后再提高到反伽马的幂-然后将该值存储在表格中
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")

    # 使用查找表应用伽玛校正
    return cv2.LUT(image, table)
```

# 三、结果图

​                                      <img src="C:/Users/kieran/Desktop/CVProgramm/%E4%BC%BD%E9%A9%AC%E5%8F%98%E6%8D%A2/original.png" style="zoom:15%;" />    

<img src="C:/Users/kieran/Desktop/CVProgramm/%E4%BC%BD%E9%A9%AC%E5%8F%98%E6%8D%A2/gamma07.png" style="zoom: 15%;" /> <img src="C:/Users/kieran/Desktop/CVProgramm/%E4%BC%BD%E9%A9%AC%E5%8F%98%E6%8D%A2/gamma15.png" style="zoom:15%;" />

# 四、结果分析

上面三幅图中：上面一张图为原图，下面的左边图为gamma = $1/0.7$的校正结果，右图为gamma = $1/1.5$的校正结果。经过gamma = $1/0.7$校正后(左图)，图像对比度降低，对比度提高(明显可以看清面容)，同时图像在的整体灰度值提高。经过gamma = $1/1.5$校正后，对比度降低(面容更不清楚了)，同时图像在的整体灰度值降低。
