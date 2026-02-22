from fastapi import APIRouter
from app.models.symptom_model import SymptomRequest, PredictionResponse
from app.services.prediction_service import predict_condition
from app.services.prediction_service import predict_disease

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
def predict(request: SymptomRequest):
    prediction = predict_disease(symptom.dict())
    return prediction
