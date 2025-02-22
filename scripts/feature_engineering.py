import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import StandardScaler, LabelEncoder
# Script ka current directory path lo
script_dir = os.path.dirname(os.path.abspath(__file__))

# Cleaned data ka path set karo
data_file_path = os.path.join(script_dir, '../data/cleaned_fraud_data.csv')

# Data load karo
df = pd.read_csv(data_file_path)
# Numerical columns ko identify karo
numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns

# Standard Scaler apply karo
scaler = StandardScaler()
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
# Categorical columns identify karo
categorical_cols = df.select_dtypes(include=['object']).columns

# Label Encoding apply karo
encoder = LabelEncoder()
for col in categorical_cols:
    df[col] = encoder.fit_transform(df[col])
    # Correlation threshold define karo
correlation_threshold = 0.01  # Weakly correlated features remove karne ke liye

# Highly correlated features select karo
correlation_matrix = df.corr()
highly_correlated_features = correlation_matrix.index[abs(correlation_matrix["Fraud Category"]) > correlation_threshold]

# Sirf important features ko retain karo
df = df[highly_correlated_features]
# Feature engineered data ka path set karo
feature_engineered_file_path = os.path.join(script_dir, '../data/feature_engineered_fraud_data.csv')

# Data save karo
df.to_csv(feature_engineered_file_path, index=False)

print(f"Feature engineered data saved at: {feature_engineered_file_path}")