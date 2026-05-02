import pandas as pd

df = pd.read_csv('vgsales_clean.csv')

df = df[["Platform", "Year", "Genre", "Publisher", "Global_Sales"]]

df = pd.get_dummies(df, columns=["Platform", "Genre", "Publisher"])

print(df.shape)
print(df.head())


df.to_csv("vgsales_features.csv", index=False)
