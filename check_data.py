import pandas as pd

df = pd.read_csv('credit_data.csv')

print("Total rows:", df.shape[0])
print("Total columns:", df.shape[1])
print()
print("Risk column breakdown:")
print(df['Risk'].value_counts())
print()
print("Percentage split:")
print(df['Risk'].value_counts(normalize=True) * 100)