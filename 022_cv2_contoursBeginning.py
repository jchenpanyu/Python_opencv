# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 14:19:20 2017

OpenCV 中的轮廓
初识轮廓
函数：cv2.findContours()，cv2.drawContours()

函数cv2.findContours() 有三个参数，第一个是输入图像，第二个是
轮廓检索模式，第三个是轮廓近似方法。返回值有三个，第一个是图像，第二个
是轮廓，第三个是（轮廓的）层析结构。轮廓（第二个返回值）是一个Python
列表，其中存储这图像中的所有轮廓。每一个轮廓都是一个Numpy 数组，包
含对象边界点（x，y）的坐标。

函数cv2.drawContours() 可以被用来绘制轮廓。它可以根据你提供
的边界点绘制任何形状。它的第一个参数是原始图像，第二个参数是轮廓，一
个Python 列表。第三个参数是轮廓的索引（在绘制独立轮廓是很有用，当设
置为-1 时绘制所有轮廓）。接下来的参数是轮廓的颜色和厚度等。

@author: vincchen
"""

from matplotlib import pyplot as plt
import cv2

img = cv2.imread('test.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 160, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


plt.subplot(121), plt.imshow(img, cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(thresh, cmap = 'gray')
plt.title('contours'), plt.xticks([]), plt.yticks([])
plt.show()