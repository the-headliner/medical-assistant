import joblib
import os
import pandas as pd

# Load model and features once (on startup)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "ml", "model.pkl")
FEATURES_PATH = os.path.join(BASE_DIR, "ml", "features.pkl")

model = joblib.load(MODEL_PATH)
feature_columns = joblib.load(FEATURES_PATH)


def predict_disease(symptom_data: dict):
    # Create ordered input list
    input_data = []

    for feature in feature_columns:
        input_data.append(symptom_data.get(feature, 0))

    # Convert to DataFrame
    input_df = pd.DataFrame([input_data], columns=feature_columns)

    # Predict
    prediction = model.predict(input_df)[0]

    return prediction