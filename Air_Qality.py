import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv(r"F:\IF6I\dsbda\AirQ.csv", encoding='cp1252')
df.describe()
print(df)
print(df.head())

print(df.info())

print(df.isnull().sum())

print("to print a number of non null values in each column")

print(df.count())

#data cleaning
print(df.columns)
print("cleaning the data by removing the less valuable columns")
df=df.drop(['stn_code', 'agency','sampling_date','location_monitoring_station'], axis = 1)  #dropping columns that aren't required

# dropping rows where no date is available
df=df.dropna(subset=['date'])

print(df.columns)

df["type"].unique()

types = {
    "Residential": "R",
    "Residential and others": "RO",
    "Residential, Rural and other Areas": "RRO",
    "Industrial Area": "I",
    "Industrial Areas": "I",
    "Industrial": "I",
    "Sensitive Area": "S",
    "Sensitive Areas": "S",
    "Sensitive": "S",
    "NaN": "RRO"
}
df.type = df.type.replace(types)

print(df.head(5))

#creating a new column year --to view the trend over a period of time ,we need year values for each row and

df['date'] = pd.to_datetime(df['date'], errors='coerce')
print(df.head(5))

df['year'] = df.date.dt.year
print(df.head(5))


#Handling Missing Values
#thee column such as SO2, NO2, rspm, spm, pm2_5 are the ones which contribute much to our analysis. So, we need to remove null from those columns to avoid inaccuracy in the prediction. We use the Imputer from sklearn.preprocessing to fill the missing values in every column with the mean.**

# defining columns of importance, which shall be used reguarly
COLS = ['so2', 'no2', 'rspm', 'spm', 'pm2_5']

import numpy as np
from sklearn.impute import SimpleImputer
# invoking SimpleImputer to fill missing values
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
df[COLS] = imputer.fit_transform(df[COLS])


print(df.head(5))

print(df.info())

print(df['type'].value_counts())


df['type'].replace({"RRO":1, "I":2, "RO":3,"S":4,"RIRUO":5,"R":6}, inplace= True)

print(df['type'])

#Converting Categorical Data to Numerical Data Using Label Encoding

print(df['state'].value_counts())

from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()
df["state"]=labelencoder.fit_transform(df["state"])
df.head(5)

dfAndhra=df[(df['state']==0)]
print(dfAndhra)

print(dfAndhra['location'].value_counts())

from sklearn.preprocessing import OneHotEncoder
onehotencoder=OneHotEncoder(sparse=False,handle_unknown='error',drop='first')


pd.DataFrame(onehotencoder.fit_transform(dfAndhra[["location"]]))
print(pd.DataFrame)