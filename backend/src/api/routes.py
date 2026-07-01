
from fastapi import APIRouter
from src.models.predictor import Predictor
from src.api.schemas import ManualPredictionRequest
from src.api.services.dashboard_service import dashboard_service
from src.explainability.shap_explainer import shap_explainer
from src.explainability.lime_explainer import lime_explainer
from src.api.services.scenario_service import scenario_service

router = APIRouter()
predictor = Predictor()

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

@router.get("/scenario/normal")
def get_normal_scenario():
    return scenario_service.normal()


@router.get("/scenario/fault")
def get_fault_scenario():
    return scenario_service.fault()

@router.get("/compare-models")
def compare_models():

    sample = dashboard_service.demo_original.iloc[
    [max(dashboard_service.index - 1, 0)]
]

    return dashboard_service.predictor.compare_models(sample)

@router.post("/predict/manual")
def manual_prediction(request: ManualPredictionRequest):

    sample = request.to_model_input()

    prediction = predictor.predict(
        sample,
        model="xgb",
    )

    lime = lime_explainer.explain(sample)

    probabilities = sorted(
        prediction["probabilities"].items(),
        key=lambda x: x[1],
        reverse=True,
    )[:3]

    return {
        "prediction": prediction["fault_name"],
        "confidence": prediction["confidence"],
        "top_predictions": [
            {
                "fault": name,
                "confidence": score,
            }
            for name, score in probabilities
        ],
        "lime": lime["top_features"],
    }