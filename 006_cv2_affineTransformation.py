# -*- coding: utf-8 -*-
"""
Created on Thu Apr 06 14:58:42 2017

图像的仿射变换
图像的仿射变换涉及到图像的形状位置角度的变化，是深度学习预处理中常到的功能
仿射变换具体到图像中的应用，主要是对图像的缩放，旋转，剪切，翻转和平移的组合
在OpenCV中，仿射变换的矩阵是一个2×3的矩阵
其中左边的2×2子矩阵是线性变换矩阵，右边的2×1的两项是平移项

A=[a00 a01   B=[b0
   a10 a11]     b1]
   
M=[A B]= [a00 a01 b0
          a10 a11 b1]

对于图像上的任一位置(x,y)，仿射变换执行的是如下的操作：
T_affine=A*[x  + B =   [x
            y]       M* y
                        1]
                        
需要注意的是，对于图像而言，宽度方向是x，高度方向是y,坐标的顺序和图像像素对应下标一致
所以原点的位置不是左下角而是右上角，y的方向也不是向上，而是向下。
在OpenCV中实现仿射变换是通过仿射变换矩阵和cv2.warpAffine()这个函数

@author: vincchen
"""

import cv2
import numpy as np

# 读取一张600x400的照片
img = cv2.imread('test_600x400_human.jpg')

# 沿着横纵轴放大1.6倍，然后平移(-150,-240)，最后沿原图大小截取，等效于裁剪并放大
M_crop = np.array([
    [1.6, 0, -150],
    [0, 1.6, -240]
], dtype=np.float32)

img_affine_1 = cv2.warpAffine(img, M_crop, (600, 400))
cv2.imwrite('006_img_affine_1.jpg', img_affine_1)

# x轴的剪切变换，角度15°
theta = 15 * np.pi / 180
M_shear = np.array([
    [1, np.tan(theta), 0],
    [0, 1, 0]
], dtype=np.float32)

img_sheared = cv2.warpAffine(img, M_shear, (600, 400))
cv2.imwrite('006_img_sheared.jpg', img_sheared)

# 顺时针旋转，角度15°
M_rotate = np.array([
    [np.cos(theta), -np.sin(theta), 0],
    [np.sin(theta), np.cos(theta), 0]
], dtype=np.float32)

img_rotated = cv2.warpAffine(img, M_rotate, (600, 400))
cv2.imwrite('006_M_rotate.jpg', img_rotated)

# 某种变换，具体旋转+缩放+旋转组合可以通过SVD分解理解
M = np.array([
    [1, 1.5, -400],
    [0.5, 2, -100]
], dtype=np.float32)

img_transformed = cv2.warpAffine(img, M, (600, 400))
cv2.imwrite('006_img_transformed.jpg', img_transformed)











