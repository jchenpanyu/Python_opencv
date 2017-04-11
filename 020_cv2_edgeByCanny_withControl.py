# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 12:18:18 2017

Canny 边缘检测

在OpenCV 中只需要一个函数：cv2.Canny()，就可以完成以上几步。
让我们看如何使用这个函数。这个函数的第一个参数是输入图像。第二和第三
个分别是minVal 和maxVal。第三个参数设置用来计算图像梯度的Sobel
卷积核的大小，默认值为3。最后一个参数是L2gradient，它可以用来设定
求梯度大小的方程。如果设为True，就会使用我们上面提到过的方程，否则
使用方程：Edge_Gradient (G) = |Gx^2| + |Gy^2|代替，默认值为False。

@author: vincchen
"""

import cv2

img = cv2.imread('resized_200x300.jpg', 0)

cv2.namedWindow('window')
def nothing(x):
    pass
cv2.createTrackbar('minVal_edge_bar', 'window', 0, 255, nothing)
cv2.createTrackbar('maxVal_edge_bar', 'window', 0, 255, nothing)

while(1):
    minVal_edge = cv2.getTrackbarPos('minVal_edge_bar', 'window')
    maxVal_edge = cv2.getTrackbarPos('maxVal_edge_bar', 'window')
    image_edges = cv2.Canny(img, minVal_edge, maxVal_edge)
    
    cv2.imshow('window', image_edges)
    
    k=cv2.waitKey(1)&0xFF
    if k==27:
        break

cv2.destroyAllWindows()