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

    x = np.linspace(1, 100, 100)
    y = [57711,50771,50133,54612,47789,49708,53595,50959,57009,48661,47509,48701,48104,48250,54825,54743,54170,48384,53561,53770,47232,48010,54735,53749,54646,48108,48371,54537,47990,49345,54591,53788,54544,54805,46326,47486,54261,49624,48912,48259,50171,47524,48085,54130,54499,53269,48358,48620,48273,54028,54748,47896,53528,53166,47656,54715,47673,46755,49569,54742,52680,47788,47935,48162,46233,54026,53750,55699,54823,50803,46553,46239,54629,52659,54527,55204,54822,46769,48696,47839,46576,53536,49658,54951,49061,50090,52384,53938,49558,53944,49749,46560,52825,49551,47968,52638,46152,54594,54756,58863]
    z = [0,50,100,0,100,50,50,50,100,50,100,50,50,50,0,0,100,0,0,0,100,50,0,0,0,50,50,0,50,0,50,0,0,100,100,50,0,50,50,50,50,50,100,0,0,50,100,0,50,100,0,50,0,100,50,0,100,100,50,100,100,50,50,100,50,50,50,0,0,50,100,100,50,0,0,0,0,50,50,100,100,100,50,0,50,50,50,0,50,50,50,100,0,50,100,100,50,50,0,50]

    y2 = [47754,47868,47181,48189,48057,47098,48282,47535,47571,47975,48197,48551,46287,48126,48503,48699,48527,47644,48096,49620,47808,49246,48740,48631,48712,47738,47985,49698,48616,47885,48526,46356,47147,46664,48483,48504,48218,49068,46969,48756,47942,48162,48540,48540,47967,48836,47716,46916,48521,47197,49730,47800,48713,48503,48183,48700,47259,47895,47776,47509,47759,48730,47536,47739,47853,49167,48057,47688,47539,47740,47902,46622,48570,47675,47800,47528,48616,47244,48795,48528,46436,48520,48651,47850,46869,47857,48057,47503,47664,48102,48087,47977,49076,48629,47858,48099,48489,48523,47564,47692]
    z2 = [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]
    #x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 50)
    #y = np.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma)
    print x.shape
    print 'x = \n', x
#    print y.shape
    print 'y = \n', y
    # plt.plot(x, y, 'ro-', linewidth=2)
    plt.plot(x, y, 'r-', label='Original',linewidth=2)
    plt.plot(x, y2, 'b-', label='Modified',linewidth=2)
    plt.grid(True)
    plt.title(u'运行时间波动图 ')
    plt.legend(loc='upper right')
    plt.show()

    plt.plot(x, z, 'r-', label='Original', linewidth=2)
    plt.plot(x, z2, 'b-', label='Modified', linewidth=2)
    plt.grid(True)
    plt.ylabel(u"本地化率%")
    plt.title(u'本地化率 ')
    plt.legend(loc='upper right')
    plt.show()


    plt.figure(figsize=(8, 8), facecolor='w')
    #3行一列，占用第一个，即是第一行第一列
    plt.subplot(211)
    plt.plot(x, y, 'g-', lw=2)
    plt.title(u'orginal', fontsize=15)
    plt.grid(True)
    plt.subplot(212)
    plt.stem(x, y, linefmt='r-', markerfmt='ro')
    plt.title(u'modified', fontsize=15)
    plt.grid(True)
    plt.tight_layout(1.5, rect=[0, 0.04, 1, 0.96])
    plt.suptitle(u'运行时间', fontsize=17)
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