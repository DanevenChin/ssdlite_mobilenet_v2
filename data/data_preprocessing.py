# -*- coding: utf-8 -*-
"""
@author  : 秦丹峰
@contact : daneven.jim@gmail.com
@license : (C) Copyright, 广州海格星航信息科技有限公司
@time    : 2020/8/4 23:23
@file    : data_preprocessing.py
@desc    : 
"""
import sys
sys.path.append("..")
from data.transforms import *


class TrainAugmentation:
    def __init__(self, size, mean=0, std=1.0):
        """
        Args:
            size: the size the of final image.
            mean: mean pixel value per channel.
        """
        self.mean = mean
        self.size = size
        self.augment = Compose([
            ConvertFromInts(),  # 图片数据int转为float32
            PhotometricDistort(),  # 随机亮度、随机对比度、随机饱和度、随机色彩、随机亮度噪声
            Expand(self.mean),  # 随机图片扩展
            RandomSampleCrop(),  # 随机裁剪
            RandomMirror(),  # 随机镜像
            ToPercentCoords(),  # 坐标归一化
            Resize(self.size),  # 图片resize
            SubtractMeans(self.mean),  # 图片减均值
            lambda img, boxes=None, labels=None: (img / std, boxes, labels),  # 图片除以方差
            ToTensor(),  # numpy -> tensor, hwc -> chw
        ])

    def __call__(self, img, boxes, labels):
        """

        Args:
            img: the output of cv.imread in RGB layout.
            boxes: boundding boxes in the form of (x1, y1, x2, y2).
            labels: labels of boxes.
        """
        return self.augment(img, boxes, labels)


class TestTransform:
    def __init__(self, size, mean=0.0, std=1.0):
        self.transform = Compose([
            ToPercentCoords(),
            Resize(size),
            SubtractMeans(mean),
            lambda img, boxes=None, labels=None: (img / std, boxes, labels),
            ToTensor(),
        ])

    def __call__(self, image, boxes, labels):
        return self.transform(image, boxes, labels)


class PredictionTransform:
    def __init__(self, size, mean=0.0, std=1.0):
        self.transform = Compose([
            Resize(size),
            SubtractMeans(mean),
            lambda img, boxes=None, labels=None: (img / std, boxes, labels),
            ToTensor()
        ])

    def __call__(self, image):
        image, _, _ = self.transform(image)
        return image