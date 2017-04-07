# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 11:33:22 2017

现在我们知道怎样将一幅图像从BGR 转换到HSV 了，我们可以利用这
一点来提取带有某个特定颜色的物体。在HSV 颜色空间中要比在BGR 空间
中更容易表示一个特定颜色


@author: vincchen
"""

import cv2
import numpy as np

img = cv2.imread('test_600x400.png')
img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 设定阈值
lower=np.array([8, 219, 239])
upper=np.array([130, 220, 240])

# 根据阈值构建掩模
mask=cv2.inRange(img_HSV, lower, upper)

# 对原图像和掩模进行位运算
res=cv2.bitwise_and(img, img_HSV, mask=mask)

# 显示图像
cv2.imshow('img', img)
cv2.imshow('mask', mask)
cv2.imshow('res', res)

cv2.waitKey(0)&0xFF
cv2.destroyAllWindows()