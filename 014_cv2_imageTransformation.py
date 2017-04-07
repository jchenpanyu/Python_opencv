# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 12:46:14 2017

几何变换

@author: vincchen
"""
import cv2
import numpy as np

img = cv2.imread('test_600x400_human.jpg')
height, width=img.shape[:2]

# 扩展缩放
# 在缩放时我们推荐使用cv2.INTER_AREA
# 扩展时我们推荐使用v2.INTER_CUBIC（慢) 和v2.INTER_LINEA
img_shrink = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
img_expand = cv2.resize(img, (2*width, 2*height), interpolation=cv2.INTER_CUBIC)

# 平移
"""
如果你要沿（x，y）方向移动，移动的距离
是（tx，ty），你可以以下面的方式构建移动矩阵：
M = [1 0 tx
     0 1 ty]
"""
tx = 100
ty = 50
M_move = np.array([[1, 0, tx], [0, 1, ty]], np.float32)
img_move = cv2.warpAffine(img, M_move, (width, height))

# 旋转
# 这里的第一个参数为旋转中心，第二个为旋转角度，第三个为旋转后的缩放因子
M_rotate = cv2.getRotationMatrix2D((width/2, height/2), 90, 0.5)
img_rotage = cv2.warpAffine(img, M_rotate, (width*2, height*2))

# 仿射变换
"""
在仿射变换中，原图中所有的平行线在结果图像中同样平行。为了创建这
个矩阵我们需要从原图像中找到三个点以及他们在输出图像中的位置。然后
cv2.getAffineTransform 会创建一个2x3 的矩阵，最后这个矩阵会被传给
函数cv2.warpAffine。
"""
pts1 = np.float32([[0, 0], [200, 50], [50,200]])
pts2=  np.float32([[10, 100], [200, 50], [100, 250]])
M_AffineTransform = cv2.getAffineTransform(pts1, pts2)
img_AffineTransform = cv2.warpAffine(img, M_AffineTransform, (width, height))

# 透视变换
"""
对于视角变换，我们需要一个3x3 变换矩阵。在变换前后直线还是直线。
要构建这个变换矩阵，你需要在输入图像上找4 个点，以及他们在输出图
像上对应的位置。这四个点中的任意三个都不能共线。这个变换矩阵可以有
函数cv2.getPerspectiveTransform() 构建。然后把这个矩阵传给函数
cv2.warpPerspective。
"""
pts3 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts4 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M_Perspective = cv2.getPerspectiveTransform(pts3, pts4)
img_Perspective = cv2.warpPerspective(img, M_Perspective, (300,300))


cv2.imshow('img', img)
cv2.imshow('img_shrink', img_shrink)
cv2.imshow('img_expand', img_expand)
cv2.imshow('img_move', img_move)
cv2.imshow('img_rotage', img_rotage)
cv2.imshow('img_AffineTransform', img_AffineTransform)
cv2.imshow('img_Perspective', img_Perspective)

cv2.waitKey(0)&0xFF
cv2.destroyAllWindows()