import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler, MinMaxScaler
df = pd.read_csv("tumhara_dataset.csv")  # Replace with actual dataset name
df.drop(columns=["Dummy Policy No", "Policy Payment Term", "Bank code"], inplace=True)
label_enc = LabelEncoder()
df["MARITALSTATUS"] = label_enc.fit_transform(df["MARITALSTATUS"])
df["INDIV_REQUIREMENTFLAG"] = label_enc.fit_transform(df["INDIV_REQUIREMENTFLAG"])
df = pd.get_dummies(df, columns=["OCCUPATION", "PREMIUMPAYMENTMODE", "NOMINEE_RELATION"], drop_first=True)
scaler = MinMaxScaler()
df[["ANNUAL_INCOME", "Premium", "ASSURED_AGE", "Policy Sum Assured"]] = scaler.fit_transform(
    df[["ANNUAL_INCOME", "Premium", "ASSURED_AGE", "Policy Sum Assured"]]
)
print(df.head())

df.to_csv("processed_data.csv", index=False)
print("✅ Feature Engineering Complete! Processed dataset saved as processed_data.csv")