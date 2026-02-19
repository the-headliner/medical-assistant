from fastapi import FastAPI
from app.routes.prediction_route import router as prediction_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Medical Assistant API is running"}

@app.get("/health")
def health_check():
    return {"status": "OK"}

app.include_router(prediction_router)
