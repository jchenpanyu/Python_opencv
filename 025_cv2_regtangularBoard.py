# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 15:34:24 2017

边界矩形

@author: vincchen
"""
import cv2

img = cv2.imread('test_poly_3.png')

im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(im_gray, 127 ,255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]

# 直边界矩形
"""
一个直矩形（就是没有旋转的矩形）。它不会考虑对象是否旋转。
所以边界矩形的面积不是最小的。可以使用函数cv2.boundingRect() 查找得到。
（x，y）为矩形左上角的坐标，（w，h）是矩形的宽和高。
"""
x,y,w,h = cv2.boundingRect(cnt)
cv2.rectangle(img, (x, y), (x+w ,y+h), (0,255,0), thickness=1)

# 旋转的边界矩形
"""
旋转的边界矩形这个边界矩形是面积最小的，因为它考虑了对象的旋转。用
到的函数为cv2.minAreaRect()。返回的是一个Box2D 结构，其中包含
矩形左上角角点的坐标（x，y），矩形的宽和高（w，h），以及旋转角度。但是
要绘制这个矩形需要矩形的4 个角点，可以通过函数cv2.boxPoints() 获得。
"""
(x, y), (w, h), angle = cv2.minAreaRect(cnt)
#cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), thickness=1)

"""
函数cv2.minEnclosingCircle() 可以帮我们找到一个对象的外切圆。
它是所有能够包括对象的圆中面积最小的一个。
"""
(x,y), radius = cv2.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
cv2.circle(img, center, radius, (255,0,0), thickness=2)

"""
使用的函数为cv2.ellipse()，返回值其实就是旋转边界矩形的内切圆。
"""
ellipse = cv2.fitEllipse(cnt)
cv2.ellipse(img, ellipse, (0,0,255), 2)


cv2.imshow('img', img)
k=cv2.waitKey(0)&0xFF
cv2.destroyAllWindows()