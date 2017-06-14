#!/usr/bin/python
# -*- coding:utf-8 -*-

# 导入NumPy函数库，一般都是用这样的形式(包括别名np，几乎是约定俗成的)
import numpy as np
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import time
from scipy.optimize import leastsq
import scipy.optimize as opt
import scipy
import matplotlib.pyplot as plt
from scipy.stats import norm, poisson
from scipy.interpolate import BarycentricInterpolator
from scipy.interpolate import CubicSpline
import math

if __name__ == "__main__":
    matplotlib.rcParams['font.sans-serif'] = [u'SimHei']  #FangSong/黑体 FangSong/KaiTi
    matplotlib.rcParams['axes.unicode_minus'] = False

    x = np.linspace(1, 5, 5)
    y = [65272,65634,59679,61609,63713]
    y2 = [61792,61912,56008,56967,56054]
    #x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 50)
    #y = np.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma)
    print x.shape
    print 'x = \n', x
#    print y.shape
    print 'y = \n', y
    # plt.plot(x, y, 'ro-', linewidth=2)
    plt.plot(x, y, 'r-', x, y, 'go', label='Original',linewidth=2, markersize=8)
    plt.plot(x, y2, 'b-', x, y2, 'y^', label='Modified',linewidth=2, markersize=8)
    plt.grid(True)
    plt.title(u'pageRank 对比图 ')
    plt.legend(loc='upper right')
    plt.show()

    plt.stem(x, y, linefmt='r-', markerfmt='ro',label='Original')
    plt.stem(x, y2, linefmt='g-', markerfmt='bo',label='Modified')
    plt.title(u'对比', fontsize=15)
    plt.grid(True)
    plt.legend(loc='upper right')
    plt.show()

    plt.bar(x,y,0.4,color="green",label=u'Original')
    plt.bar(x, y2, 0.4, color="red",label='Modified')
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("bar chart")
    plt.legend(loc='upper right')
    plt.show()



    plt.figure(figsize=(8, 8), facecolor='w')
    #3行一列，占用第一个，即是第一行第一列
    plt.subplot(311)
    plt.plot(x, y, 'g-', lw=2)
    plt.title(u'图1', fontsize=15)
    plt.grid(True)
    plt.subplot(312)
    plt.stem(x, y, linefmt='r-', markerfmt='ro')
    plt.title(u'图2', fontsize=15)
    plt.grid(True)
    plt.subplot(313)
    plt.plot(x, y, 'b-', lw=2, markersize=4)
    plt.title(u'图3', fontsize=15)
    plt.grid(True)
    plt.tight_layout(1.5, rect=[0, 0.04, 1, 0.96])
    plt.suptitle(u'三图汇总', fontsize=17)
    plt.show()