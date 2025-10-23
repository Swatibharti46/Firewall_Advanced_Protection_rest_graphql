import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Sample training data (you can later connect it to live traffic)
data = {
    "requests_per_min": [5, 6, 7, 8, 100, 6, 7, 120, 130, 8],
    "avg_response_time": [100, 120, 110, 115, 3000, 130, 140, 4000, 3500, 125],
}
df = pd.DataFrame(data)

# Train the model
model = IsolationForest(contamination=0.2, random_state=42)
model.fit(df)

# Save model
joblib.dump(model, "firewall_anomaly_model.pkl")
print("✅ Model trained and saved as firewall_anomaly_model.pkl")
