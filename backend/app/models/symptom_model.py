from pydantic import BaseModel
from typing import List

class SymptomRequest(BaseModel):
    symptoms: List[str]

class PredictionResponse(BaseModel):
    predicted_condition: str
    confidence: float
