import pandas as pd

# Dataset Load
df = pd.read_csv('../data/fraud_data_2023_24.csv')

# Missing Values Handle
df.fillna(method='ffill', inplace=True)

# Unnecessary Columns Drop
df.drop(columns=['Unnamed: 0'], errors='ignore', inplace=True)

# Categorical Variables Encoding
df = pd.get_dummies(df, drop_first=True)

# Cleaned Data Save
df.to_csv('../data/cleaned_fraud_data.csv', index=False)

print("Data Preprocessing Completed!")