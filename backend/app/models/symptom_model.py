from pydantic import BaseModel


class SymptomRequest(BaseModel):
    fever: int
    cough: int
    headache: int
    nausea: int
    fatigue: int


class PredictionResponse(BaseModel):
    disease: str