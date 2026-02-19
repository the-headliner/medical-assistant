from fastapi import APIRouter
from app.models.symptom_model import SymptomRequest, PredictionResponse
from app.services.prediction_service import predict_condition

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
def predict(request: SymptomRequest):
    result = predict_condition(request.symptoms)
    return result
