# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 09:59:56 2017

形态学转换
腐蚀，膨胀，开运算，闭运算等
cv2.erode()，cv2.dilate()，cv2.morphologyEx()

@author: vincchen
"""

import cv2
import numpy as np

img = cv2.imread('test_bw_j.JPG', 0)

kernel = np.ones((5,5), np.uint8)
# 结构化元素
"""
在前面的例子中我们使用Numpy 构建了结构化元素，它是正方形的。但
有时我们需要构建一个椭圆形/圆形的核。为了实现这种要求，提供了OpenCV
函数cv2.getStructuringElement()。你只需要告诉他你需要的核的形状
和大小。
"""
# Rectangular Kernel
# cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
# Elliptical Kernel
# cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
# Cross-shaped Kernel
# cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))


# 腐蚀
"""
这个操作会把前景物体的边界腐蚀掉（但是前景仍然
是白色）。这是怎么做到的呢？卷积核沿着图像滑动，如果与卷积核对应的原图
像的所有像素值都是1，那么中心元素就保持原来的像素值，否则就变为零。
这回产生什么影响呢？根据卷积核的大小靠近前景的所有像素都会被腐蚀
掉（变为0），所以前景物体会变小，整幅图像的白色区域会减少。这对于去除
白噪声很有用，也可以用来断开两个连在一块的物体等。
"""
img_erosion = cv2.erode(img, kernel, iterations = 1)

# 膨胀
"""
与腐蚀相反，与卷积核对应的原图像的像素值中只要有一个是1，中心元
素的像素值就是1。所以这个操作会增加图像中的白色区域（前景）。一般在去
噪声时先用腐蚀再用膨胀。因为腐蚀在去掉白噪声的同时，也会使前景对象变
小。所以我们再对他进行膨胀。这时噪声已经被去除了，不会再回来了，但是
前景还在并会增加。膨胀也可以用来连接两个分开的物体。
"""
img_dilation = cv2.dilate(img, kernel, iterations = 1)

# 开运算
"""
先进性腐蚀再进行膨胀就叫做开运算。就像我们上面介绍的那样，它被用
来去除噪声。这里我们用到的函数是cv2.morphologyEx()。
"""
img_2 = cv2.imread('test_bw_j_2.JPG')
img_opening = cv2.morphologyEx(img_2, cv2.MORPH_OPEN, kernel)

# 闭运算
"""
先膨胀再腐蚀。它经常被用来填充前景物体中的小洞，或者前景物体上的小黑点。
"""
img_3 = cv2.imread('test_bw_j_3.JPG')
img_closing = cv2.morphologyEx(img_3, cv2.MORPH_CLOSE, kernel)

# 形态学梯度
"""
其实就是一幅图像膨胀与腐蚀的差别。
结果看上去就像前景物体的轮廓。
"""
img_gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# 礼帽
"""
原始图像与进行开运算之后得到的图像的差。下面的例子是用一个9x9 的
核进行礼帽操作的结果。
"""
img_tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# 黑帽
"""
进行闭运算之后得到的图像与原始图像的差。
"""
img_blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow('img', img)
cv2.imshow('img_erosion', img_erosion)
cv2.imshow('img_dilation', img_dilation)
cv2.imshow('img_gradient', img_gradient)
cv2.imshow('img_tophat', img_tophat)

cv2.imshow('img_2', img_2)
cv2.imshow('img_opening', img_opening)

cv2.imshow('img_3', img_3)
cv2.imshow('img_closing', img_closing)

cv2.waitKey(0)&0xFF
cv2.destroyAllWindows()
