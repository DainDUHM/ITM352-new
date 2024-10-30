import pandas as pd


file_path = 'C:\Users\User\Documents\GitHub\ITM352_Fall24_repo\Lab10\DBMS_labwork.pptx'
df = pd.read_json(file_path)


print("DataFrame:")
print(df)


print("\nSummary Statistics:")
print(df.describe())

print("\nMedian Values:")
print(df.median())
