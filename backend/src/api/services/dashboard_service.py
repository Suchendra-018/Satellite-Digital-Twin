from src.models.predictor import Predictor
from src.data.dataset import (
    load_demo_scaled,
    load_demo_original,
)


class DashboardService:

    HEALTH_SCORE = {
        "Normal": 100,
        "Power Anomaly": 80,
        "Battery Degradation": 75,
        "Reaction Wheel Fault": 70,
        "Thermal Fault": 65,
        "Communication Fault": 60,
        "Sensor Fault": 85,
    }

    ALERT_LEVEL = {
        "Normal": "NORMAL",
        "Power Anomaly": "WARNING",
        "Battery Degradation": "WARNING",
        "Reaction Wheel Fault": "CRITICAL",
        "Thermal Fault": "CRITICAL",
        "Communication Fault": "WARNING",
        "Sensor Fault": "WARNING",
    }

    def __init__(self):
        self.predictor = Predictor()

        self.demo_scaled = load_demo_scaled()
        self.demo_original = load_demo_original()

        self.index = 0
        self.history = []

    def get_dashboard_data(self):

        if self.index >= len(self.demo_original):
            self.index = 0

        scaled_sample = self.demo_scaled.iloc[[self.index]]
        original_sample = self.demo_original.iloc[[self.index]]

        prediction = self.predictor.predict(
            scaled_sample,
            model="xgb",
        )

        telemetry = original_sample.iloc[0].to_dict()

        fault_name = prediction["fault_name"]
        confidence = round(prediction["confidence"], 2)

        health_score = self.HEALTH_SCORE.get(fault_name, 70)
        alert_level = self.ALERT_LEVEL.get(fault_name, "WARNING")

        history_item = {
            "sample": self.index + 1,
            "fault": fault_name,
            "confidence": confidence,
            "health_score": health_score,
        }

        self.history.append(history_item)

        if len(self.history) > 100:
            self.history.pop(0)

        response = {
            "prediction": prediction,
            "telemetry": telemetry,
            "confidence": confidence,
            "health_score": health_score,
            "alert_level": alert_level,
            "sample": self.index + 1,
            "total_samples": len(self.demo_original),
            "history": self.history[-20:],
        }

        self.index += 1

        return response


dashboard_service = DashboardService()