#
import numpy as np
import pandas as pd
import seaborn as sns

Air = pd.read_csv(r"C:\Users\Aditya\Downloads\dsbda\AirGraph.csv", sep=';')

print(Air.head())

print(Air.info())

Air = Air.iloc[:,:-2]


Air.replace(to_replace=',',value='.',regex=True,inplace=True)

columns_to_convert = ['CO(GT)','C6H6(GT)', 'T', 'RH', 'AH']
for column in columns_to_convert:
    Air[column] = pd.to_numeric(Air[column], errors='coerce')

Air.replace(-200,np.nan,inplace=True)
print(Air.info())

Air.drop('NMHC(GT)', axis=1, inplace=True)
Air['Date'] = pd.to_datetime(Air['Date'], format='%d/%m/%Y')
Air['Time'] = pd.to_datetime(Air['Time'], format='%H.%M.%S').dt.time
Air.describe()

import matplotlib.pyplot as plt
numerical_columns = Air.select_dtypes(include=[np.number]).columns

for column in numerical_columns:
    plt.figure(figsize=(6,3))
    sns.boxplot(x=Air[column])
    plt.title(f'Boxplot of {column}')
    plt.show()

for column in numerical_columns:
    plt.figure(figsize=(6, 3))
    sns.histplot(x=Air[column], stat="count", color="blue", bins=15, kde={'alpha': 0.5})
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

sns.pairplot(Air, diag_kind='kde')
plt.show()

Air = Air.apply(lambda column: column.interpolate(method="linear") if column.dtype != 'datetime64[ns]' and column.dtype != '<m8[ns]' else column)



for column in numerical_columns:
    plt.figure(figsize=(6,3))
    sns.histplot(x=Air[column], stat="count", color="blue", bins=15, kde={'alpha': 0.5})
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')

format(len(Air[Air.duplicated()]))

plt.figure(figsize=(15,10))
sns.heatmap(Air.corr(method='pearson', min_periods=1),annot=True)

