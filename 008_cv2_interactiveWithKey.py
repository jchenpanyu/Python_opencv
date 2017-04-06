# -*- coding: utf-8 -*-
"""
Created on Thu Apr 06 17:15:00 2017

下面的程序将会加载一个灰度图，显示图片，
按下’s’键保存后退出，或者
按下ESC 键退出不保存。

@author: vincchen
"""

import cv2

img = cv2.imread('test_600x400.png', 1) # 0: grad mode, 1: RGB mode

cv2.imshow('title: Image', img)

key = cv2.waitKey(0)&0xFF
if key == 27: # wait for 'Esc' to exit
    cv2.destroyAllWindows()
elif key == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('cv2saveimg.png', img)
    cv2.destroyAllWindows()