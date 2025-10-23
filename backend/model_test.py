# model_test.py — tests the anomaly detector with different samples
from ml_model import AnomalyDetector

detector = AnomalyDetector()
samples = [
    [0.2, 0.1, -0.3],
    [5.1, 3.2, 0.9],   # likely anomaly
    [-0.1, 0.0, 0.2]
]

for s in samples:
    print(f"Sample {s} → Anomaly: {detector.is_anomaly(s)}")
