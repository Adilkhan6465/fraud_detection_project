# 🛡️ Insurance Fraud Detection using Machine Learning

This project is focused on building a machine learning model to detect fraudulent financial transactions based on patterns in the data.

## 📌 Problem Statement

To detect and classify **insurance claims** as fraudulent or genuine using supervised learning techniques.
Insurance frauds are often hidden and lead to huge financial losses in the insurance sector.  
The goal is to train a machine learning model to recognize patterns that typically indicate fraud.

## 🧠 Technologies & Libraries Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook
- Matplotlib / Seaborn (for data visualization)

## 📊 Project Workflow

1. **Data Loading & Preprocessing**
   - Handled missing/null values
   - Feature selection and encoding
   - Scaling and normalization

2. **Exploratory Data Analysis**
   - Distribution plots
   - Class imbalance analysis
   - Correlation matrix

3. **Model Building**
   - Used **Logistic Regression** for classification
   - Split data into training and test sets
   - Fit the model and evaluated results

4. **Evaluation Metrics**
   - Accuracy Score
   - Confusion Matrix
   - Precision & Recall

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/Adilkhan6465/fraud_detection_project.git

## 📈 Results

- **Accuracy Achieved**: 93.12%
- The model shows strong performance in identifying fraudulent transactions.
- Further tuning and use of ensemble models may improve performance slightly.

## folder structure 

fraud-detection-project/


├── data/                          --> all datasets 
│   ├── insurance_data.csv
│   ├── fraud data FY 2023-24.csv
│   └── feature_engineered_fraud_data.csv
│
├── models/                        --> save trained model 
│   └── fraud_detection_model.pkl
│
├── scripts/                       -->  (training, preprocessing etc.)
│   ├── model_training.py
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   └── app.py
│
├── test_api.py                    --> API test
├── requirements.txt               --> Python libraries list
├── README.md                      --> 

## 🔮 Future Improvements

- Implement advanced models like Random Forest, XGBoost, or SVM
- Handle class imbalance using SMOTE or undersampling
- Create a web interface using Flask/Streamlit for real-time predictions
- Add model explainability (SHAP/LIME)

## 👨‍💻 Author

**Adil Khan**  
GitHub: [github.com/Adilkhan6465](https://github.com/Adilkhan6465)

---

