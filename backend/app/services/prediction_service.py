def predict_condition(symptoms: list[str]) -> dict:
    """
    Temporary rule-based logic.
    Later this will be replaced by ML model.
    """

    if "fever" in symptoms and "cough" in symptoms:
        return {
            "predicted_condition": "Flu",
            "confidence": 0.85
        }

    if "headache" in symptoms:
        return {
            "predicted_condition": "Migraine",
            "confidence": 0.75
        }

    return {
        "predicted_condition": "Unknown",
        "confidence": 0.50
    }
