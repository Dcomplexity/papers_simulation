import numpy as np
import matplotlib.pyplot as plt
import string
# from sympy import *
#
# x = Symbol("x")
# print (diff(1 / (1 + x**2), x))


xData = np.arange(0, 100, 1)
# yData1 = 12 * xData.__pow__(0.8) - 4 * xData - 0.0001 * (99 * xData).__pow__(1.5)
yData1 = xData / (2 - (1 / ((xData - 1) * 1 + 1)))
# yData2 = np.arange(15, 61, 5)
plt.figure(num=1, figsize=(8,6))
plt.title('Plot 1', size=14)
plt.xlabel('x-axis', size=14)
plt.ylabel('y-axis', size=14)
plt.plot(xData, yData1, color='b', linestyle='--', marker='o', label='y1 data')
# plt.plot(xData, yData2, color='r', linestyle='-', label='y2 data')
plt.legend(loc='upper left')
plt.show()