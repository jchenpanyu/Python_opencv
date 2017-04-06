# -*- coding: utf-8 -*-
# -*- coding:gb2312 -*-
"""
Created on Wed Apr 05 17:48:18 2017

@author: vincchen
"""

import cv2
img = cv2.imread(r'C:\Users\vincchen\Documents\7_Coding\Python\test\Python_opencv\test.png')
cv2.imshow('hello', img)
cv2.waitKey(2000)