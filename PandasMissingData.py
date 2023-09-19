import numpy as np
import pandas as pd

#creating dictionary with list values
d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}

# puttimg in DataFrames format
df = pd.DataFrame(d)

print(df)

#line break
print()

#lot of times we want to drop missing values
# NOTE: dropna() will have by-default axis as 0, which means it will drop the rows if it has nan
print(df.dropna())
print()
print(df.dropna(axis=1))
print()

#Threshold, for non na, means it should have atleast thresh to drop the row
print(df.dropna(thresh=2))
print()

#fillna
print(df.fillna(value='10'))
print()
print(df.fillna(value=df['A'].mean()))