import pandas as pd
import numpy as np

df = pd.read_csv(r"F:\IF6I\dsbda\dataset_Facebook.csv", sep=";")
df.describe()
print(df)
print(df.shape)
df1=df[['Page total likes','Category','Post Month','Post Weekday']].loc[0:15]
df2=df[['Page total likes','Category','Post Month','Post Weekday']].loc[16:30]
df3=df[['Page total likes','Category','Post Month','Post Weekday']].loc[31:50]
print(df1)




print("Here is merged data")
print("merging data")
merging = pd.concat([df1,df2,df3])
print(merging)


print("here is sorted data")
print("Sorting data")
sort_values= df.sort_values('Page total likes', ascending=False)
print(sort_values)


print("Here is tranpose data")
print("transpose")
df.transpose()

print("shape and reshape")
shaping = df.shape
print(shaping)

print("reshaping the data")
pivot_table = pd.pivot_table(df, index = ['Type','Category'], values='comment')
print(pivot_table)



