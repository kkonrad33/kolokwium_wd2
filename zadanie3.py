import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
import xlrd

df = pd.read_csv('cars.csv', header=0, sep=';')
y = df[(df['Model year'] > 71) & (df['Model year'] < 78)].groupby(['Model year']).agg({'Model year': ['count']})
wykres = y.plot.bar()
plt.xticks(rotation=0)
plt.ylabel("Ilość aut")
plt.xlabel("Rocznik")
plt.title('Ilość aut w latach')
plt.show()