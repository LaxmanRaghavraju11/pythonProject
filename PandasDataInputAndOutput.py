#CSV files
#Excel files
#HTML web
#SQL

#pip install sqlalchemy
#pip install lxml
#pip install html5lib
#pip install BeautifulSoup4
#pip install xlrd

import pandas as pd

# pd.read_csv('filecsv.csv')
# print(pd.read_clipboard())

#it will copy dataframe to excel
#df.to_excel('excelName.xlsx',sheet='sheet1')

data = pd.read_html('http://www.google.com')
print(data)

#pandas arent the best to read sql bcos there are many flavors of sql
#THis will create a very simple engine

from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')

# df.to_sql('myTable',engine)
# sqlread = pd.read_sql('myTable',engine)