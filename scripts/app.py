import logging
from flask import Flask, request, jsonify
import joblib
import pandas as pd

# ✅ Logging setup
logging.basicConfig(filename="app.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

logging.info("✅ Flask API started...")

app = Flask(__name__)

# ✅ Model load karo
model = joblib.load("models/fraud_detection_model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        logging.info(f"📩 Received request: {data}")  # ✅ Request log

        df = pd.DataFrame([data])
        prediction = model.predict(df)

        logging.info(f"✅ Prediction: {prediction[0]}")  # ✅ Prediction log
        return jsonify({'fraud_prediction': int(prediction[0])})

    except Exception as e:
        logging.error(f"❌ Error: {str(e)}")  # ✅ Error log
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)