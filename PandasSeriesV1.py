import numpy as np
import pandas as pd

#series in pandas

labels = ['america','brasil','canada','India']
my_data = [10,20,30,40]

# it will auto label as 01234.. if not given
my_data_series = pd.Series(my_data)
labels_series = pd.Series(labels)
#if labels given it will give labels
my_data_labels_series = pd.Series(my_data,labels)

print(my_data_series)
print(labels_series)
print(my_data_labels_series)

# addition of series
print(my_data_labels_series + my_data_labels_series)

#dictionaries to series

d = {'key1' : 'keyValue1','key2' : 'keyValue2','key3' : 3 }

dict_series = pd.Series(d)

print(dict_series)