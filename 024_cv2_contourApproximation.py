# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 15:22:15 2017

轮廓近似

将轮廓形状近似到另外一种由更少点组成的轮廓形状，新轮廓的点的数目
由我们设定的准确度来决定。使用的Douglas-Peucker算法，你可以到维基百
科获得更多此算法的细节。
为了帮助理解，假设我们要在一幅图像中查找一个矩形，但是由于图像的
种种原因，我们不能得到一个完美的矩形，而是一个“坏形状”（如下图所示）。
现在你就可以使用这个函数来近似这个形状（）了。这个函数的第二个参数叫
epsilon，它是从原始轮廓到近似轮廓的最大距离。它是一个准确度参数。选
择一个好的epsilon 对于得到满意结果非常重要。s

@author: vincchen
"""

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('test_poly_2.JPG', 0)

ret, thresh = cv2.threshold(img, 240 ,255, 0)
contours, hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]
epsilon = 0.01*cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, epsilon, True)
"""
plt.subplot(131), plt.imshow(img, cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(thresh, cmap = 'gray')
plt.title('contours'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(thresh, cmap = 'gray')
plt.title('thresh'), plt.xticks([]), plt.yticks([])
plt.show()
"""
# 程序不完整