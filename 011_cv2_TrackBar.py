# -*- coding: utf-8 -*-
"""
Created on Thu Apr 06 18:08:32 2017

用滑动条做调色板
cv2.getTrackbarPos()，cv2.creatTrackbar()

cv2.getTrackbarPos() 函数的一个参数是滑动条的名字，第二个参数
是滑动条被放置窗口的名字，第三个参数是滑动条的默认位置。第四个参数是
滑动条的最大值，第五个函数是回调函数，每次滑动条的滑动都会调用回调函
数。回调函数通常都会含有一个默认参数，就是滑动条的位置。在本例中这个
函数不用做任何事情，我们只需要pass 就可以了

@author: vincchen
"""

import cv2
import numpy as np

def nothing(x):
    pass

# 创建一副黑色图像
img=np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)

switch='0:OFF\n1:ON'
cv2.createTrackbar(switch,'image',0,1,nothing)

while(1):
    cv2.imshow('image', img)
    k=cv2.waitKey(1)&0xFF
    if k==27:
        break
    r=cv2.getTrackbarPos('R','image')
    g=cv2.getTrackbarPos('G','image')
    b=cv2.getTrackbarPos('B','image')
    s=cv2.getTrackbarPos(switch,'image')
    if s==0:
        img[:]=0
    else:
        img[:]=[b,g,r]

cv2.destroyAllWindows()