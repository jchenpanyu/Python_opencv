# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 13:51:49 2017

图像金字塔
cv2.pyrUp()，cv2.pyrDown()

有两类图像金字塔：高斯金字塔和拉普拉斯金字塔。
高斯金字塔的顶部是通过将底部图像中的连续的行和列去除得到的。顶
部图像中的每个像素值等于下一层图像中5 个像素的高斯加权平均值。这样
操作一次一个MxN 的图像就变成了一个M/2xN/2 的图像。所以这幅图像
的面积就变为原来图像面积的四分之一。这被称为Octave。连续进行这样
的操作我们就会得到一个分辨率不断下降的图像金字塔。我们可以使用函数
cv2.pyrDown() 和cv2.pyrUp() 构建图像金字塔。

cv2.pyrDown() 从一个高分辨率大尺寸的图像向上构建一个金子塔（尺寸变小，分辨率降低）。
cv2.pyrUp() 从一个低分辨率小尺寸的图像向下构建一个金子塔（尺寸变大，但分辨率不会增加）。

@author: vincchen
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('face.jpg')

img_pyrDown = cv2.pyrDown(img)
img_pyrDown_2 = cv2.pyrDown(img_pyrDown)

img_pyrup = cv2.pyrDown(img, 6)
img_pyrup_2 = cv2.pyrDown(img)

print 'img.shape=', img.shape
print 'img_pyrDown.shape=', img.shape
print 'img_pyrDown_2.shape=', img_pyrDown_2.shape
print 'img_pyrup.shape=', img_pyrup.shape
print 'img_pyrup_2.shape=', img.shape

plt.subplot(231),plt.imshow(img)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(232),plt.imshow(img_pyrDown)
plt.title('img_pyrDown'), plt.xticks([]), plt.yticks([])
plt.subplot(233),plt.imshow(img_pyrDown_2)
plt.title('img_pyrDown_2'), plt.xticks([]), plt.yticks([])

plt.subplot(235),plt.imshow(img_pyrup)
plt.title('img_pyrup'), plt.xticks([]), plt.yticks([])
plt.subplot(236),plt.imshow(img_pyrup_2)
plt.title('img_pyrup_2'), plt.xticks([]), plt.yticks([])

plt.show()