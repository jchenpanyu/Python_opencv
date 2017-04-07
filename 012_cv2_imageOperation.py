# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 10:34:13 2017

图像上的算术运算

@author: vincchen
"""

import cv2
import numpy as np

img_1 = cv2.imread(r'C:\Users\vincchen\Documents\7_Coding\Python\test\Python_opencv\test_600x400.png')
img_2 = cv2.imread(r'C:\Users\vincchen\Documents\7_Coding\Python\test\Python_opencv\test_600x400_human.jpg')

# 图像加法
# OpenCV 中的加法与Numpy 的加法是有所不同的。
# OpenCV 的加法是一种饱和操作，而Numpy 的加法是一种模操作。

img_add = img_1 + img_2

cv2.imshow('img_add', img_add)
key = cv2.waitKey(0)&0xFF
if key == 27: # wait for 'Esc' to exit
    cv2.destroyAllWindows()

# 权重图像混合

img_weight = cv2.addWeighted(img_1, 0.3, img_2, 0.7, 0)
cv2.imshow('img_weight', img_weight)
key = cv2.waitKey(0)&0xFF
if key == 27: # wait for 'Esc' to exit
    cv2.destroyAllWindows()

# 按位运算
# 把img 1的火箭贴到图2上
rows, cols, channels = img_1.shape
roi = img_2[0:rows, 0:cols]

# 制造火箭对于的mask跟inverse mask
img2gray = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 127, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
# 取roi 中与mask 中不为零的值对应的像素的值，其他值为0
# 注意这里必须有mask=mask 或者mask=mask_inv, 其中的mask= 不能忽略
img_bg = cv2.bitwise_and(roi, roi, mask = mask)
# 取roi 中与mask_inv 中不为零的值对应的像素的值，其他值为0。
# Take only region of logo from logo image.
img_fg = cv2.bitwise_and(img_1, img_1, mask = mask_inv)

# Put logo in ROI and modify the main image
dst = cv2.add(img_bg,img_fg)
img_2[0:rows, 0:cols ] = dst
cv2.imshow('res',img_2)
cv2.waitKey(0)&0xFF
cv2.destroyAllWindows()










