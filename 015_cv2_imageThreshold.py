# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 12:48:16 2017

图像阈值
简单阈值，自适应阈值，Otsu’s 二值化等
有cv2.threshold，cv2.adaptiveThreshold 等。

@author: vincchen
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test_imwrite.png', 0) # read imag, grad mode

# 全局阈值 cv2.threshhold()。
"""
这个函数的第一个参数就是原图像，原图像应该是灰度图。
第二个参数就是用来对像素值进行分类的阈值。
第三个参数就是当像素值高于（有时是小于）阈值时应该被赋予的新的像素值。
OpenCV提供了多种不同的阈值方法，这是有第四个参数来决定的。
• cv2.THRESH_BINARY
• cv2.THRESH_BINARY_INV
• cv2.THRESH_TRUNC
• cv2.THRESH_TOZERO
• cv2.THRESH_TOZERO_INV
"""
ret, thresh1=cv2.threshold(img, 126, 255, cv2.THRESH_BINARY)
ret, thresh2=cv2.threshold(img, 126, 255, cv2.THRESH_BINARY_INV)
ret, thresh3=cv2.threshold(img, 126, 255, cv2.THRESH_TRUNC)
ret, thresh4=cv2.threshold(img, 126, 255, cv2.THRESH_TOZERO)
ret, thresh5=cv2.threshold(img, 126, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

plt.figure(figsize=(14, 6))
for i in xrange(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()


# 自适应阈值
"""
此时的阈值是根据图像上的每一个小区域计算与其对应的阈值。
因此在同一幅图像上的不同区域采用的是不同的阈值，从而使我们能在亮度不同的情况下得到更好的结果。
这种方法需要我们指定三个参数，返回值只有一个。
• Adaptive Method- 指定计算阈值的方法。
– cv2.ADPTIVE_THRESH_MEAN_C：阈值取自相邻区域的平均值
– cv2.ADPTIVE_THRESH_GAUSSIAN_C：阈值取值相邻区域的加权和，权重为一个高斯窗口。
• Block Size - 邻域大小（用来计算阈值的区域大小）。
• C - 这就是是一个常数，阈值就等于的平均值或者加权平均值减去这个常数。
"""
img_2=cv2.imread('test_word_200x200.jpg', 0) # read imag, grad mode

ret, img_2_thre = cv2.threshold(img_2, 127, 255, cv2.THRESH_BINARY)
#10为Block size, 2 为c值
img_2_threMEAN = cv2.adaptiveThreshold(img_2, 255, cv2.ADAPTIVE_THRESH_MEAN_C,\
                                       cv2.THRESH_BINARY, 11, 2)
img_2_threGAUSSIAN= cv2.adaptiveThreshold(img_2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                                          cv2.THRESH_BINARY, 11, 2)

titles_2 = ['Original Image', 'Global Thresholding (v = 127)',
          'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images_2 = [img_2, img_2_thre, img_2_threMEAN, img_2_threGAUSSIAN]

plt.figure(figsize=(14, 6))
for i in xrange(4):
    plt.subplot(2,2,i+1), plt.imshow(images_2[i], 'gray')
    plt.title(titles_2[i])
    plt.xticks([]),plt.yticks([])
plt.show()


# Otsu’s 二值化
"""
在使用全局阈值时，我们就是随便给了一个数来做阈值，那我们怎么知道
我们选取的这个数的好坏呢？答案就是不停的尝试。如果是一副双峰图像（简
单来说双峰图像是指图像直方图中存在两个峰）呢？我们岂不是应该在两个峰
之间的峰谷选一个值作为阈值？这就是Otsu 二值化要做的。简单来说就是对
一副双峰图像自动根据其直方图计算出一个阈值。（对于非双峰图像，这种方法
得到的结果可能会不理想）。
这里用到到的函数还是cv2.threshold()，但是需要多传入一个参数
（flag）：cv2.THRESH_OTSU。这时要把阈值设为0。然后算法会找到最
优阈值，这个最优阈值就是返回值retVal。如果不使用Otsu 二值化，返回的
retVal 值与设定的阈值相等。
下面的例子中，输入图像是一副带有噪声的图像。第一种方法，我们设
127 为全局阈值。第二种方法，我们直接使用Otsu 二值化。第三种方法，我
们首先使用一个5x5 的高斯核除去噪音，然后再使用Otsu 二值化。看看噪音
去除对结果的影响有多大吧。
"""

# gobal threshold is the 1st part

# Otsu's thresholding
ret, thresh_Otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# Otsu's thresholding after Gaussian filtering
#（5,5）为高斯核的大小，0 为标准差
blur = cv2.GaussianBlur(img, (5,5), 0)
ret, thresh_Otsu_Gaussian = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# plot all the images and their histograms
images_3 = [img, 0, thresh1,
            img, 0, thresh_Otsu,
            blur, 0, thresh_Otsu_Gaussian]
titles_3 = ['Original Noisy Image', 'Histogram', 'Global Thresholding (v=126)',
            'Original Noisy Image', 'Histogram', 'Otsu Thresholding',
            'Gaussian filtered Image', 'Histogram', 'Otsu Thresholding']
plt.figure(figsize=(15, 6))
for i in xrange(3):
    plt.subplot(3, 3, i*3+1), plt.imshow(images_3[i*3], 'gray')
    plt.title(titles_3[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 3, i*3+2), plt.hist(images_3[i*3].ravel(), 256)
    plt.title(titles_3[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 3, i*3+3), plt.imshow(images_3[i*3+2], 'gray')
    plt.title(titles_3[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()
