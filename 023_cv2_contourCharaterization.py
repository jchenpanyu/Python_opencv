# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 14:54:47 2017

轮廓特征
查找轮廓的不同特征，例如面积，周长，重心，边界框等。

@author: vincchen
"""

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('test_poly.jpg', 0)

"""
图像的矩可以帮助我们计算图像的质心，面积等。详细信息请查看维基百科Image Moments。
函数cv2.moments() 会将计算得到的矩以一个字典的形式返回
"""

ret, thresh = cv2.threshold(img, 120 ,255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
M = cv2.moments(cnt)

"""
根据这些矩的值，我们可以计算出对象的重心：
Cx=M10/M00, Cy=M01/M00
"""
Cx = int(M['m10'] / M['m00'])
Cy = int(M['m01'] / M['m00'])

"""
轮廓的面积可以使用函数cv2.contourArea() 计算得
也可以使用矩（0 阶矩），M['m00']。
"""
area = cv2.contourArea(cnt)

"""
轮廓周长也被称为弧长。可以使用函数cv2.arcLength() 计算得到。这个函数
的第二参数可以用来指定对象的形状是闭合的（True），还是打开的（一条曲线）。
"""
perimeter = cv2.arcLength(cnt, True)

plt.subplot(111), plt.imshow(thresh, cmap = 'gray')
plt.title('contours'), plt.xticks([]), plt.yticks([])
plt.show()