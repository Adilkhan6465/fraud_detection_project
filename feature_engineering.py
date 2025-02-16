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