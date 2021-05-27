import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl
from math import *
x = np.arange(-2.0, 10, 0.2)
y = -4*(x**2)+((6*x)/2)+20
plt.subplot(3, 1, 1)
plt.plot(x, y, 'ro')
plt.axis([-2, 4, -25, 25])
plt.grid()
plt.title('Pierwszy wykres')


plt.subplot(3, 1, 2)
y = np.tan(x)-5
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axis([-2, 6, -40, 80])
plt.grid()
plt.title('Drugi wykres')

plt.subplot(3, 1, 3)
y = np.arange(-100, 100, 0.1)
plt.plot(y, (-4)*y**2+(6*y/2)+20, 'ro')
plt.plot(y, np.tan(y)-5)
plt.axis([-2, 6, -100, 100])
plt.title('Trzeci wykres')
plt.grid()
plt.show()