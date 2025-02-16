import pandas as pd

# CSV file ko read karein with error handling
try:
    insurance_df = pd.read_csv('insurance_data.csv', encoding='ISO-8859-1', on_bad_lines='skip', engine='python')
    fraud_df = pd.read_csv('Fraud data FY 2023-24 for B&CC.csv', encoding='ISO-8859-1', on_bad_lines='skip', engine='python')
    print(insurance_df.head())
    print(fraud_df.head())
except pd.errors.ParserError as e:
    print(f"ParserError: {e}")
except Exception as e:
    print(f"Error: {e}")
    
import pandas as pd
import numpy as np

# CSV Files Load
insurance_df = pd.read_csv('insurance_data.csv')
fraud_df = pd.read_csv('Fraud data FY 2023-24 for B&CC.csv')

# 1. Missing Values Handle Karein
insurance_df.fillna(0, inplace=True)
fraud_df.fillna(0, inplace=True)

# 2. Date Column Ko Convert Karein (sirf insurance_df me hai)
insurance_df['TXN_DATE_TIME'] = pd.to_datetime(insurance_df['TXN_DATE_TIME'])

# 3. Fraud Flag Add Karein
fraud_df['is_fraud'] = 1
insurance_df['is_fraud'] = 0

# 4. Fraud Data me Ek Dummy TXN_DATE_TIME Column Add Karein
fraud_df['TXN_DATE_TIME'] = pd.NaT

# 5. Dono Dataframes Ko Merge Karein
combined_df = pd.concat([insurance_df, fraud_df], ignore_index=True)

# 6. New Feature: Transaction Hour (sirf valid dates par)
combined_df['transaction_hour'] = combined_df['TXN_DATE_TIME'].dt.hour.fillna(-1)

# 7. Result Save Karein
combined_df.to_csv('combined_fraud_dataset.csv', index=False)

print("Feature Engineering Complete! Combined dataset saved.")   