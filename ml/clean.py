import pandas as pd

df = pd.read_csv('vgsales.csv')

df = df.dropna(subset=["Year", "Publisher"])

df["Year"] = df["Year"].astype(int)

print(df.shape)
print(df.isnull().sum())


df.to_csv("vgsales_clean.csv", index=False)

print("Hello")