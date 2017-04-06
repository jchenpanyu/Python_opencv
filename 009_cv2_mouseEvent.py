# -*- coding: utf-8 -*-
"""
Created on Thu Apr 06 17:39:05 2017

你将要学习的函数是：cv2.setMouseCallback()
这里我们来创建一个简单的程序，他会在图片上你双击过的位置绘制一个圆圈。

@author: vincchen
"""

import cv2
import numpy as np

def draw_circle(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 1000, (0, 0, 0), -1)

img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(True):
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF ==27:
        break
cv2.destroyAllWindows()