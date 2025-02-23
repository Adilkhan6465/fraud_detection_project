import pandas as pd

# Data Load
df = pd.read_csv("data/feature_engineered_fraud_data.csv")
# X (features) aur Y (target) split karna
X = df.drop(columns=['Fraud Category'])  # Features
y = df['Fraud Category']  # Target label
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
from sklearn.ensemble import RandomForestClassifier

# Model initialize karna
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Model train karna
model.fit(X_train, y_train)
from sklearn.metrics import accuracy_score

# Prediction karna
y_pred = model.predict(X_test)

# Accuracy check karna
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
import joblib  # Model save karne ke liye

# Model ko save karo
joblib.dump(model, "models/fraud_detection_model.pkl")

print("Model saved successfully!")