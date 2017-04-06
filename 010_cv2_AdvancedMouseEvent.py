# -*- coding: utf-8 -*-
"""
Created on Thu Apr 06 17:39:05 2017

你将要学习的函数是：cv2.setMouseCallback()
这里我们来创建一个简单的程序，他会在图片上你双击过的位置绘制一个圆圈。

@author: vincchen
"""

import cv2
import numpy as np

# 当鼠标按下时变为True
drawing = False
# 如果mode 为true 绘制矩形。按下'm' 变成绘制曲线。
mode = True
ix,iy = -1,-1

# 创建回调函数
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    # 当按下左键是返回起始位置坐标
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    # 当鼠标左键按下并移动是绘制图形。event可以查看移动，flag查看是否按下
    elif event == cv2.EVENT_MOUSEMOVE and flags==cv2.EVENT_FLAG_LBUTTON:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                # 绘制圆圈，小圆点连在一起就成了线，3 代表了笔画的粗细
                cv2.circle(img,(x,y),3,(0,0,255),-1)
    # 当鼠标松开停止绘画。
    elif event==cv2.EVENT_LBUTTONUP:
        drawing==False
    
img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1)&0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
cv2.destroyAllWindows()