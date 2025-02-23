from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Model load karo
model = joblib.load("models/fraud_detection_model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        df = pd.DataFrame([data])
        prediction = model.predict(df)
        return jsonify({'fraud_prediction': int(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)