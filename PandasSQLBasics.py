import numpy as np
import pandas as pd

data = {'Company':['GOOGLE','FB','APPLE','GOOGLE','FB','APPLE'],
        'Person':['Sam','Ram','Jose','Gandhi','Modi','Ryan'],
        'Sales':[1000,2000,3000,4000,5000,6000]}

df = pd.DataFrame(data)

print(df)
print()
print(df.groupby('Company'))
print()
print(df.groupby('Company').sum())
print()
# print(df.groupby('Company').std())
# print()
# print(df.groupby('Company').loc('FB').sum())
# print()
print((df.groupby('Company')).count())
print()
print(df.groupby('Company').describe())
print()
print(df.groupby('Company').describe().transpose())

#merge
leftDF = pd.DataFrame(data)
rightDF = pd.DataFrame(data)

print()
print(pd.merge(leftDF,rightDF,how='inner',on='Company'))

leftDF.join(rightDF)
leftDF.join(rightDF,how='outer')

df[''].unique()
#number of unique values
df[''].nunique()

#how many times each values appeared in df
df[''].value_counts()

#apply method

def times2(x):
        return x*2

df['col2'].apply(times2)

df['col2'].apply(lambda x : x*2)

#names of col
df.columns

#names of indexs
df.index

df.sort_values('col2')

df.isnull()

df.pivot_table(values='D',index=['A','B'],columns=['C'])