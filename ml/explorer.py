import pandas as pd

df = pd.read_csv('vgsales.csv')

print(df.shape)
print(df.head())
print(df.dtypes)
print(df.isnull().sum())
print("Hello")
