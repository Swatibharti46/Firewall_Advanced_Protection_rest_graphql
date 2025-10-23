import joblib
import numpy as np

model = joblib.load("ml_module/firewall_anomaly_model.pkl")

def detect_anomaly(requests_per_min, avg_response_time):
    data = np.array([[requests_per_min, avg_response_time]])
    prediction = model.predict(data)
    return "Anomaly Detected" if prediction[0] == -1 else "Normal"
