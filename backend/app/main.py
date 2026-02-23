from fastapi import FastAPI
from app.routes.prediction_route import router as prediction_router

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all origins for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Medical Assistant API is running"}

@app.get("/health")
def health_check():
    return {"status": "OK"}

app.include_router(prediction_router)
