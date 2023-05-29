import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('F:\IF6I\DSBDA1/heartGraph.csv')
print(df.head())

print(df.describe())

plt.hist(df['age'], bins = [20,30,40,50,60,70,80], edgecolor = 'black')
plt.title('Age')
plt.show()

plt.hist(df['trtbps'], bins = [90,100,110,120,130,140,150,160,170,180,190,200], edgecolor = 'black')
plt.title('Resting Blood Pressure')
plt.show()

plt.hist(df['chol'], bins = 7, edgecolor = 'black')
plt.title('Cholesterol')
plt.show()

plt.hist(df['thall'], bins = [70,80,90,100,110,120,130,140,150,160,170,180,190,200], edgecolor = 'black')
plt.title('Max Heart Rate')
plt.show()

plt.hist(df['oldpeak'], bins = 5, edgecolor = 'black')
plt.title('ST Depression')
plt.show()

plt.scatter(df['age'],df['trtbps'], s=30, c = '#b6eb7a', edgecolor = 'green', linewidth = 1, alpha = 0.8)
plt.xlabel('Age')
plt.ylabel('Resting Blood Pressure')
plt.title('Age vs RBP')
plt.show()

plt.scatter(df['age'],df['chol'], s=30, c = '#9bdeac', edgecolor = 'green', linewidth = 1, alpha = 0.8)
plt.xlabel('Age')
plt.ylabel('Cholesterol')
plt.title('Age vs Cholesterol')
plt.show()

plt.scatter(df['age'],df['thall'], s=30, c = '#b6eb7a', edgecolor = 'green', linewidth = 1, alpha = 0.8)
plt.xlabel('Age')
plt.ylabel('Max Heart Rate')
plt.title('Age vs Max Heart Rate')
plt.show()

plt.scatter(df['age'],df['oldpeak'], s=30, c = '#a8df65', edgecolor = 'green', linewidth = 1, alpha = 0.8)
plt.xlabel('Age')
plt.ylabel('ST depression')
plt.title('Age vs ST depsression')
plt.show()

sns.jointplot(x=df['chol'], y=df['trtbps'], data=df, kind="kde")
plt.show()

sns.jointplot(x=df['thall'], y=df['chol'], data=df)
plt.show()

plt.scatter(df['trtbps'],df['thall'], s=30, c = '#e2979c', edgecolor = 'red', linewidth = 1, alpha = 0.9)
plt.xlabel('Resting Blood Pressure')
plt.ylabel('Max Heart Rate')
plt.title('RBP vs Max Heart Rate')
plt.show()

plt.figure( figsize = (10,10))
sns.heatmap(df.corr(), annot = True)
plt.show()