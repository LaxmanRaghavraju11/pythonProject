import numpy as np
import pandas as pd

from numpy.random import randn as rdn

#Dataframes in pandas

#this method seed will always get same values everytime and any where
np.random.seed(101)

#here DataFrames is taking 2d random array, row labels, column labels
df = pd.DataFrame(rdn(5,4),['A','B','C','D','E'],['z','y','x','w'])

print(df)

#will return type of df which is series
type(df['z'])

print(df[['z','y']])

#create new columm
df['new1'] = df['w'] + df['z']

print(df)

#axis = 0 is rows
#axis =1 is column
#inplace will modify in main object too
df.drop('new1',axis=1,inplace=True)

print(df)

df.drop('A',axis=0)

print(df)

df_B = df.loc['B']
print(df_B)

df_B_C = df.loc['B','z']
print(df_B_C)

df_chunk = df.loc[['A','B'],['x','w']]
print(df_chunk)


# iloc is for getting by integer, here in below code it will fail
# df_B = df.iloc['B']

#conditional selection on dataframe

print(df>0)

print(df[df>0])

print(df['w']>0)

#whereever the value in w is less then 0 it will eliminate that row and return whole df
print(df[df['w']>0])

print(df[df['w']>0]['x'])

print(df[df['w']>0][['x','y']])

#DATA FRAMES PART 2 -- > multiple conditions

#whereever the value in w is less then 0 and value in y less then 1 it will eliminate that rows and return whole df
print(df[(df['w']>0) & (df['y'] > 1) ])

print(df.reset_index())

#trict to quickly create list
new_index = 'ind us eng pak aus'.split()

print(new_index)

df['country'] = new_index

print(df)

#to set new_index as index
df.set_index('country',inplace=True)
print(df)

#DATA FRAMES PART 3 -- > multi index

#Index levels

outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]

#This will give couple of tuples of outside and inside
hier_index = list(zip(outside,inside))
print(hier_index)

hier_index = pd.MultiIndex.from_tuples(hier_index)
print(hier_index)

multiLevelIndex_df = pd.DataFrame(rdn(6,2),hier_index,['A','B'])
print(multiLevelIndex_df)

print(multiLevelIndex_df.loc['G1'])

print(multiLevelIndex_df.loc['G1'].loc[1])

multiLevelIndex_df.index.names = ['GROUPS','NUM']

print(multiLevelIndex_df)

print(multiLevelIndex_df.loc['G1'].loc[1]['B'])

print(multiLevelIndex_df.xs('G2'))

# xs = cross-section
#for level NUM it will get 1 num row for all groups
print(multiLevelIndex_df.xs(1,level='NUM'))