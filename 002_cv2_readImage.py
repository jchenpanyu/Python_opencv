# -*- coding: utf-8 -*-
"""
Created on Thu Apr 06 12:22:01 2017

读图像用cv2.imread()，可以按照不同模式读取
一般最常用到的是读取单通道灰度图，或者直接默认读取多通道。
存图像用cv2.imwrite()，注意存的时候是没有单通道这一说的，
根据保存文件名的后缀和当前的array维度，OpenCV自动判断存的通道，
另外压缩格式还可以指定存储质量，
来看代码例子：

@author: vincchen
"""

import cv2

# 读取一张图像
color_img = cv2.imread('face.jpg')
print(color_img.shape)

# 直接读取单通道
gray_img = cv2.imread('face.jpg', cv2.IMREAD_GRAYSCALE)
print(gray_img.shape)

# 把单通道图片保存后，再读取，仍然是3通道，相当于把单通道值复制到3个通道保存
cv2.imwrite('test_grayscale.jpg', gray_img)
reload_grayscale = cv2.imread('test_grayscale.jpg')
print(reload_grayscale.shape)

# cv2.IMWRITE_JPEG_QUALITY指定jpg质量，范围0到100，默认95，越高画质越好，文件越大
cv2.imwrite('test_imwrite.jpg', color_img, (cv2.IMWRITE_JPEG_QUALITY, 80))

# cv2.IMWRITE_PNG_COMPRESSION指定png质量，范围0到9，默认3，越高文件越小，画质越差
cv2.imwrite('test_imwrite.png', color_img, (cv2.IMWRITE_PNG_COMPRESSION, 5))