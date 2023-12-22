#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 21:07:12 2018
@author: lisir
"""

import numpy as np
import os
from PIL import Image
import matplotlib.pyplot as plt


# 定义卷积操作的函数
def conv(image, weight):
    height, width = image.shape
    h, w = weight.shape
    # 经滑动卷积操作后得到的新的图像的尺寸
    new_h = height - h + 1
    new_w = width - w + 1
    new_image = np.zeros((new_h, new_w), dtype=np.float)
    # 进行卷积操作,实则是对应的窗口覆盖下的矩阵对应元素值相乘,卷积操作
    for i in range(new_w):
        for j in range(new_h):
            new_image[i, j] = np.sum(image[i:i + h, j:j + w] * weight)
    # 去掉矩阵乘法后的小于0的和大于255的原值,重置为0和255
    new_image = new_image.clip(0, 255)
    new_image = np.rint(new_image).astype('uint8')
    return new_image


if __name__ == "__main__":
    # 读取图像数据并且转换为对应的numpy下的数组
    A = Image.open("test2.png", 'r')
    output_path = "./outputPic2/"
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    a = np.array(A)
    # sobel算子,分别是水平方向,垂直方向和不分方向
    sobel_x = np.array(([-1, 0, 1], [-2, 0, 2], [-1, 0, 1]))
    sobel_y = np.array(([-1, -2, -1], [0, 0, 0], [1, 2, 1]))
    sobel = np.array(([-1, -1, 0], [-1, 0, 1], [0, 1, 1]))
    # prewitt各个方向上的算子
    prewitt_x = np.array(([-1, 0, 1], [-1, 0, 1], [-1, 0, 1]))
    prewitt_y = np.array(([-1, -1, -1], [0, 0, 0], [1, 1, 1]))
    prewitt = np.array(([-2, -1, 0], [-1, 0, 1], [0, 1, 2]))
    # 拉普拉斯算子
    laplacian = np.array(([0, -1, 0], [-1, 4, -1], [0, -1, 0]))
    laplacian_2 = np.array(([-1, -1, -1], [-1, 8, -1], [-1, -1, -1]))
    weight_list = ("sobel_x", "sobel_y", "sobel", "prewitt_x", "prewitt_y", "prewitt", "laplacian", "laplacian_2")

    print("Gridient detection\n")
    for w in weight_list:
        print("starting %s...." % w)
        print("weight:\n")
        print("R\n")
        R = conv(a[:, :, 0], eval(w))
        print("G\n")
        G = conv(a[:, :, 1], eval(w))
        print("B\n")
        B = conv(a[:, :, 2], eval(w))

        I = np.stack((R, G, B), axis=2)
        Image.fromarray(I).save("%s//bigger-%s.jpg" % (output_path, w))