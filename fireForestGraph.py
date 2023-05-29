#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

data = pd.read_csv(r'C:\Users\Aditya\Downloads\dsbda\FireForestGraph.csv')
print(data.head(5))

print(data.info())

print(data.describe().T)

print(data.isnull().sum())

print(data["year"].unique())


per_year = data.groupby("year")["number"].sum().reset_index()
print(per_year)

fig = plt.subplots(figsize=(15, 5))
sns.lineplot(per_year, x="year", y="number",color="#d0bbff")
plt.show()

#Let's find out how many per month
per_month = data.groupby("month",)["number"].sum().reset_index().sort_values('number', ascending = False)



fig = plt.subplots(figsize=(7,5))
sns.barplot(data=per_month, x="month",y="number")
plt.show()

#Let's find out how many per state
per_state = data.groupby("state")["number"].sum().reset_index()

plt.figure(figsize=(25,10))
sns.barplot(data=per_state, x="state",y="number")
plt.show()

df = data.drop(['date', 'month'], axis = 1)
per_state_year = df.groupby(['year', 'state'])["number"].sum().reset_index()

fig = plt.subplots(figsize=(20,10))
sns.lineplot(data=per_state_year, x="year", y="number", hue="state")
plt.show()

fig, ax = plt.subplots(figsize=(15,8))
sns.barplot(data= df.sort_values(by='number', ascending=False), x = 'number', y= 'state', ci=None, ax=ax)
ax.set_xticks(ticks=[])
ax.bar_label(ax.containers[0])
plt.title('Fires per state from 1998 to 2017', fontdict={'fontsize':20})
plt.ylabel('')
plt.style.use('ggplot')
plt.show()