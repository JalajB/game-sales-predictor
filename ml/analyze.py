import pandas as pd

df = pd.read_csv('vgsales_clean.csv')

print(df.columns.tolist())
print(df.describe())
print("Hello")