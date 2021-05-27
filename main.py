#grupa B
#zadanie 1
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
import xlrd

df = pd.read_csv('cars.csv', header=0, sep=';')
df.to_csv('plik.csv', index=False)
ndf = (df[df['Horsepower'] > 105])
mdf = df.groupby(['Model year']).agg({'Model year':['count']})
wykres = mdf.plot.pie(subplots=True, autopct='%.2f %%', fontsize=7, title= "Ilość aut w danych latach.", legend=False)
plt.savefig('auta_w_latach.png')





