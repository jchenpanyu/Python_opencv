# -*- coding: utf-8 -*-
"""
Created on Thu Apr 06 12:22:01 2017

缩放通过cv2.resize()实现，裁剪则是利用array自身的下标截取实现，
此外OpenCV还可以给图像补边，这样能对一幅图像的形状和感兴趣区域实现各种操作。
下面的例子中读取一幅400×600分辨率的图片，并执行一些基础的操作：

@author: vincchen
"""

import cv2

# 读取一张照片
img = cv2.imread('face.jpg')

# 缩放成具体像素比例的图像 300x200
img_300x200 = cv2.resize(img, (300, 200))

# 不直接指定缩放后大小，通过fx和fy指定缩放比例，0.25则长宽都为原来1/4
# 插值方法默认是cv2.INTER_LINEAR，这里指定为最近邻插值
img_025 = cv2.resize(img, (0, 0), fx=0.25, fy=0.25, 
                              interpolation=cv2.INTER_NEAREST)

# 在上张图片的基础上，上下各贴50像素的黑边，生成300x300的图像
img_025_blackside = cv2.copyMakeBorder(img, 50, 50, 0, 0, 
                                       cv2.BORDER_CONSTANT, 
                                       value=(0, 0, 0))

# 对照片中的某部分进行剪裁
patch_img = img[20:150, -180:-50]

cv2.imwrite('003_patch_img.jpg', patch_img)
cv2.imwrite('003_img_300x200.jpg', img_300x200)
cv2.imwrite('003_img_025.jpg', img_025)
cv2.imwrite('003_img_025_blackside.jpg', img_025_blackside)