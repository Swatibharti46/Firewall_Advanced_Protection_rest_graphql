# ml_model.py  —  ML-based anomaly detector
import numpy as np
from sklearn.ensemble import IsolationForest
import joblib
import os

class AnomalyDetector:
    def __init__(self, model_path="ml_model.pkl"):
        self.model_path = model_path
        self.model = None
        if os.path.exists(self.model_path):
            self.model = joblib.load(self.model_path)
        else:
            self.train_initial_model()

    def train_initial_model(self):
        # Simulate normal API request data
        normal = np.random.normal(0, 1, (200, 3))
        self.model = IsolationForest(contamination=0.1, random_state=42)
        self.model.fit(normal)
        joblib.dump(self.model, self.model_path)

    def is_anomaly(self, features):
        features = np.array(features).reshape(1, -1)
        return bool(self.model.predict(features)[0] == -1)

if __name__ == "__main__":
    detector = AnomalyDetector()
    sample = [0.5, 0.2, -0.1]
    print("Anomaly:", detector.is_anomaly(sample))
