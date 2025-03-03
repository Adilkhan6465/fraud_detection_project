import pandas as pd
import os

# Script ke current directory ka path lein
script_dir = os.path.dirname(os.path.abspath(__file__))

# Data file ka full path banayein
data_file_path = os.path.join(script_dir, '../data/Fraud data FY 2023-24 for B&CC.csv')

# CSV file load karein
df = pd.read_csv(data_file_path)

# Pehle 5 rows print karein
print(df.head())

# Numeric columns me se commas remove karein
num_cols = ["Annual Income", "Premium", "POLICY SUMASSURED"]  # Apne dataset ke numeric columns check karein
for col in num_cols:
    df[col] = df[col].astype(str).str.replace(",", "").astype(float)

# Cleaned data ko new CSV file me save karein
cleaned_file_path = os.path.join(script_dir, '../data/cleaned_fraud_data.csv')
df.to_csv(cleaned_file_path, index=False)

print(f"Cleaned data saved at: {cleaned_file_path}")