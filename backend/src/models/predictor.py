from pathlib import Path

import joblib
import pandas as pd
from shap import sample
import tensorflow as tf

from src.data.dataset import FEATURE_COLUMNS


PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODEL_DIR = PROJECT_ROOT / "saved_models"

RF_MODEL = MODEL_DIR / "random_forest.pkl"
XGB_MODEL = MODEL_DIR / "xgboost.pkl"
LSTM_MODEL = MODEL_DIR / "lstm.keras"

SCALER = MODEL_DIR / "scaler.pkl"

CLASS_NAMES = {
    0: "Normal",
    1: "Battery Degradation",
    2: "Communication Fault",
    3: "Power Anomaly",
    4: "Reaction Wheel Fault",
    5: "Sensor Fault",
    6: "Thermal Fault",
}


class Predictor:

    def __init__(self):
        self.scaler = joblib.load(SCALER)

        self.rf = joblib.load(RF_MODEL)
        self.xgb = joblib.load(XGB_MODEL)
        self.lstm = tf.keras.models.load_model(LSTM_MODEL)

    def _prepare(self, sample):

        if isinstance(sample, dict):
            sample = pd.DataFrame([sample])

        elif isinstance(sample, pd.Series):
            sample = sample.to_frame().T

        sample = sample[FEATURE_COLUMNS].copy()

        for col in FEATURE_COLUMNS:
            sample[col] = pd.to_numeric(sample[col], errors="coerce")

        return sample.astype(float)
    
    def _scale(self, sample):
        sample = sample.copy()

        sample[FEATURE_COLUMNS] = self.scaler.transform(
        sample[FEATURE_COLUMNS]
    )
        return sample

    def predict(self, sample, model="xgb"):

        sample = self._prepare(sample)
        sample = self._scale(sample)

        model = model.lower()

        if model == "rf":

            probabilities = self.rf.predict_proba(sample)[0]
            prediction = int(probabilities.argmax())

        elif model == "xgb":

            probabilities = self.xgb.predict_proba(sample)[0]
            prediction = int(probabilities.argmax())

        elif model == "lstm":

            x = sample.values.reshape(
                1,
                1,
                len(FEATURE_COLUMNS),
            )

            probabilities = self.lstm.predict(
                x,
                verbose=0,
            )[0]

            prediction = int(probabilities.argmax())

        else:
            raise ValueError(
                "Model must be rf, xgb or lstm"
            )

        confidence = float(probabilities.max() * 100)

        probability_map = {
            CLASS_NAMES[i]: round(float(probabilities[i]) * 100, 2)
            for i in range(len(CLASS_NAMES))
        }

        return {
            "fault_id": prediction,
            "fault_name": CLASS_NAMES.get(
                prediction,
                "Unknown",
            ),
            "confidence": round(confidence, 2),
            "probabilities": probability_map,
        }

    def compare_models(self, sample):

        xgb = self.predict(sample, "xgb")
        lstm = self.predict(sample, "lstm")

        return {
            "xgboost": xgb,
            "lstm": lstm,
        }


if __name__ == "__main__":

    from src.data.dataset import load_demo_original
    predictor = Predictor()
    sample = load_demo_original().iloc[[0]]

    print(predictor.compare_models(sample))