# -*- coding: utf-8 -*-
"""
@author  : 秦丹峰
@contact : daneven.jim@gmail.com
@time    : 2020/8/6 8:52
@file    : output_big_img.py
@desc    : 
"""
import os
import cv2
import numpy as np

img_path = "saved_model/img_result"
img_list = os.listdir(img_path)

row = []
column = []
for img_name in img_list:
    path = img_path+'/'+img_name
    img = cv2.imread(path)
    h, w, _= img.shape
    if h != 720 and w != 1280:
        continue

    column.append(img)

    if len(column) == 4:
        for i in range(len(column)):
            if i == 0:
                cat_img = column[i]
                continue
            cat_img = np.concatenate((cat_img, column[i]), 1)
        row.append(cat_img)
        column = []

for i in range(len(row)):
    if i == 0:
        big_img = row[i]
        continue
    big_img = np.concatenate((big_img, row[i]), 0)

height, width, _ = big_img.shape
big_img = cv2.resize(big_img, (1280, height*1280//width), interpolation=cv2.INTER_CUBIC)

cv2.imwrite("test.png", big_img)



