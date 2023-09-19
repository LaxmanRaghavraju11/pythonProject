import pandas as pd

sal = pd.read_csv('Salaries.csv')

print(sal.head())

print(sal.info())

print(sal['BasePay'])

print(sal.loc[sal['TotalPayBenefits'].argmax()])

print(sal.loc[sal['TotalPayBenefits'].idxmin()])

