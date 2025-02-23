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
    prediction_mapping = {
    0: "Not Fraud",
    1: "Potential Fraud",
    2: "Highly Fraudulent"
}


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if isinstance(data, list):  # Agar multiple inputs aaye
        predictions = [model.predict([d])[0] for d in data]
        response = [{"fraud_prediction": prediction_mapping.get(pred, "Unknown")} for pred in predictions]
    else:  # Single input
        prediction = model.predict([data])[0]
        response = {"fraud_prediction": prediction_mapping.get(prediction, "Unknown")}
    return jsonify(response)