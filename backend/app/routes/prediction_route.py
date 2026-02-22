from fastapi import APIRouter
from app.models.symptom_model import SymptomRequest, PredictionResponse
from app.services.prediction_service import predict_disease

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
def predict(symptom: SymptomRequest):
    
    prediction = predict_disease(symptom.model_dump())

    return PredictionResponse(disease=prediction)