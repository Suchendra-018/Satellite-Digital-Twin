from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.models.predictor import Predictor
from src.data.dataset import (
    load_demo_scaled,
    load_demo_original,
)

app = FastAPI(
    title="Satellite Digital Twin API",
    version="1.0.0",
)

# Enable React frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load everything once
app.state.predictor = Predictor()
app.state.demo_scaled = load_demo_scaled()
app.state.demo_original = load_demo_original()


@app.get("/")
def root():
    return {
        "message": "Satellite Digital Twin API Running"
    }


@app.get("/api/dashboard")
def get_dashboard():

    predictor = app.state.predictor

    scaled_sample = app.state.demo_scaled.iloc[[0]]
    original_sample = app.state.demo_original.iloc[[0]]

    prediction = predictor.predict(
        scaled_sample,
        model="xgb"
    )

    return {
        "prediction": prediction,
        "telemetry": original_sample.iloc[0].to_dict()
    }