# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 17:01:40 2017

图像平滑

@author: vincchen
"""

import cv2
import numpy as np

img = cv2.imread('test_imwrite.png')
h, w = img.shape[:2]
img = cv2.resize(img, (w/2, h/2))
img_noise = img + np.random.standard_normal((h/2, w/2, 3))*25
img_noise = img_noise.astype(np.uint8)

# 2D卷积
kernel_1 = np.ones((5,5), np.float32)/25
img_ave = cv2.filter2D(img, -1, kernel_1)

# blur
img_blur = cv2.blur(img, (5, 5))

# 高斯模糊
"""
现在把卷积核换成高斯核（简单来说，方框不变，将原来每个方框的值是
相等的，现在里面的值是符合高斯分布的，方框中心的值最大，其余方框根据
距离中心元素的距离递减，构成一个高斯小山包。原来的求平均数现在变成求
加权平均数，全就是方框里的值）。实现的函数是cv2.GaussianBlur()。我
们需要指定高斯核的宽和高（必须是奇数）。以及高斯函数沿X，Y 方向的标准
差。如果我们只指定了X 方向的的标准差，Y 方向也会取相同值。如果两个标
准差都是0，那么函数会根据核函数的大小自己计算。高斯滤波可以有效的从
图像中去除高斯噪音。
"""
#0 是指根据窗口大小（5,5）来计算高斯函数标准差
img_GaussianBlur = cv2.GaussianBlur(img, (5,5), 0)

# 中值模糊
"""
顾名思义就是用与卷积框对应像素的中值来替代中心像素的值。这个滤波
器经常用来去除椒盐噪声。前面的滤波器都是用计算得到的一个新值来取代中
心像素的值，而中值滤波是用中心像素周围（也可以使他本身）的值来取代他。
他能有效的去除噪声。卷积核的大小也应该是一个奇数。
在这个例子中，我们给原始图像加上50% 的噪声然后再使用中值模糊。
"""
img_noise_median = cv2.medianBlur(img_noise, 5)
img_noise_median_twice = cv2.medianBlur(img_noise_median, 5)

# 双边滤波
"""
函数cv2.bilateralFilter() 能在保持边界清晰的情况下有效的去除噪
音。但是这种操作与其他滤波器相比会比较慢。我们已经知道高斯滤波器是求
中心点邻近区域像素的高斯加权平均值。这种高斯滤波器只考虑像素之间的空
间关系，而不会考虑像素值之间的关系（像素的相似度）。所以这种方法不会考
虑一个像素是否位于边界。因此边界也会别模糊掉，而这正不是我们想要。
双边滤波在同时使用空间高斯权重和灰度值相似性高斯权重。空间高斯函
数确保只有邻近区域的像素对中心点有影响，灰度值相似性高斯函数确保只有
与中心像素灰度值相近的才会被用来做模糊运算。所以这种方法会确保边界不
会被模糊掉，因为边界处的灰度值变化比较大。
"""
#9 邻域直径，两个75 分别是空间高斯函数标准差，灰度值相似性高斯函数标准差
img_bilateralFilter =cv2.bilateralFilter(img, 9, 75, 75)

cv2.imshow('img', img)
cv2.imshow('img_ave', img_ave)
cv2.imshow('img_blur', img_blur)
cv2.imshow('img_GaussianBlur', img_GaussianBlur)
cv2.imshow('img_noise', img_noise)
cv2.imshow('img_noise_median', img_noise_median)
cv2.imshow('img_noise_median_twice', img_noise_median_twice)
cv2.imshow('img_bilateralFilter', img_bilateralFilter)
cv2.waitKey(0)&0xFF
cv2.destroyAllWindows()