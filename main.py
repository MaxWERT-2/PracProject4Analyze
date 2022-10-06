import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

COL_COUNT = 1350

mpl.rcParams.update(mpl.rcParamsDefault)

data = pd.read_excel("Base4.xlsx")
data1 = data[:COL_COUNT]
data2 = data[COL_COUNT:]

prod_count1 = 0
prod_count2 = 0
def_count1 = 0
def_count2 = 0
for i in range(COL_COUNT):
    prod_count1 += data1['produced'][i]
    prod_count2 += data2['produced'][COL_COUNT + i]
    def_count1 += data1['defects'][i]
    def_count2 += data2['defects'][COL_COUNT + i]

print(prod_count1, prod_count2, def_count1, def_count2)

fig1, axes1 = plt.subplots(1, 1, figsize=(7, 3))

sns.set_style('darkgrid')
sns.countplot(y='supplier', data=data, palette='colorblind', ax=axes1)
fig1.savefig('count.png')

fig2, axes2 = plt.subplots(1, 1, figsize=(7, 3))
sns.barplot(x=["harpy.co", "westeros.inc"], y=[prod_count1, prod_count2], palette='colorblind', ax=axes2)
fig2.savefig('produced.png')

fig3, axes3 = plt.subplots(1, 1, figsize=(7, 3))
sns.barplot(x=["harpy.co", "westeros.inc"], y=[def_count1, def_count2], palette='colorblind', ax=axes3)
fig3.savefig('defect.png')

plt.show()


