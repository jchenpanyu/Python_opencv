# -*- coding: utf-8 -*-
"""
Created on Thu Apr 06 14:30:08 2017

色调，明暗，直方图和Gamma曲线
除了区域，图像本身的属性操作也非常多，比如可以通过HSV空间对色调和明暗进行调节。
SV空间是由美国的图形学专家A. R. Smith提出的一种颜色空间，HSV分别是色调（Hue），
饱和度（Saturation）和明度（Value）。在HSV空间中进行调节就避免了直接在RGB空间中
调节是还需要考虑三个通道的相关性。OpenCV中H的取值是[0, 180)，其他两个通道的取值都
是[0, 256)，下面例子接着上面例子代码，通过HSV空间对图像进行调整：

@author: vincchen
"""

import cv2

# 读取一张照片
img = cv2.imread('face.jpg')

# 通过cv2.cvtColor把图像从BGR转换到HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# H空间中，绿色比黄色的值高一点，所以给每个像素+15，黄色的像素就会变绿
turn_green_hsv = img_hsv.copy()
turn_green_hsv[:, :, 0] = (turn_green_hsv[:, :, 0]+15) % 180
turn_green_img = cv2.cvtColor(turn_green_hsv, cv2.COLOR_HSV2BGR)
cv2.imwrite('004_turn_green.jpg', turn_green_img)

# 减小饱和度会让图像损失鲜艳，变得更灰
colorless_hsv = img_hsv.copy()
colorless_hsv[:, :, 1] = 0.5 * colorless_hsv[:, :, 1]
colorless_img = cv2.cvtColor(colorless_hsv, cv2.COLOR_HSV2BGR)
cv2.imwrite('004_colorless.jpg', colorless_img)

# 减小明度为原来一半
darker_hsv = img_hsv.copy()
darker_hsv[:, :, 2] = 0.5 * darker_hsv[:, :, 2]
darker_img = cv2.cvtColor(darker_hsv, cv2.COLOR_HSV2BGR)
cv2.imwrite('004_darker.jpg', darker_img)