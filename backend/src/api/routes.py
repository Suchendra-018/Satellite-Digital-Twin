from fastapi import APIRouter

from src.api.services.dashboard_service import dashboard_service
from src.explainability.shap_explainer import shap_explainer
from src.explainability.lime_explainer import lime_explainer

router = APIRouter()


@router.get("/dashboard")
def get_dashboard():
    return dashboard_service.get_dashboard_data()


@router.get("/telemetry")
def get_telemetry():
    data = dashboard_service.get_dashboard_data()
    return data["telemetry"]


@router.get("/prediction")
def get_prediction():
    data = dashboard_service.get_dashboard_data()

    return {
        "prediction": data["prediction"],
        "confidence": data["confidence"],
        "health_score": data["health_score"],
        "alert_level": data["alert_level"],
    }


@router.get("/history")
def get_history():
    return dashboard_service.history


@router.get("/status")
def get_status():
    return {
        "mission": "CubeSat-1",
        "system": "ONLINE",
        "digital_twin": "RUNNING",
        "telemetry": "LIVE",
        "models": {
            "xgboost": "READY",
            "lstm": "READY",
            "shap": "READY",
            "lime": "READY",
        },
    }


@router.get("/shap")
def get_shap():

    sample = dashboard_service.demo_scaled.iloc[
        [max(dashboard_service.index - 1, 0)]
    ]

    return shap_explainer.explain(sample)


@router.get("/lime")
def get_lime():

    sample = dashboard_service.demo_scaled.iloc[
        [max(dashboard_service.index - 1, 0)]
    ]

    return lime_explainer.explain(sample)


@router.get("/compare-models")
def compare_models():

    sample = dashboard_service.demo_scaled.iloc[
        [max(dashboard_service.index - 1, 0)]
    ]

    return dashboard_service.predictor.compare_models(sample)