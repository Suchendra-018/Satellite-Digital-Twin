from pathlib import Path

import joblib
import pandas as pd
import tensorflow as tf

PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODEL_DIR = PROJECT_ROOT / "saved_models"

RF_MODEL = MODEL_DIR / "random_forest.pkl"
XGB_MODEL = MODEL_DIR / "xgboost.pkl"
LSTM_MODEL = MODEL_DIR / "lstm.keras"

FEATURE_COLUMNS = [
    "OrbitPhase (%)",
    "Sunlight (0 or 1)",
    "BusVoltage (V)",
    "BusCurrent (A)",
    "BatteryVoltage (V)",
    "BatteryTemperature (°C)",
    "BatterySOC (%)",
    "SolarVoltage (V)",
    "SolarCurrent (A)",
    "WheelRPM (RPM)",
    "WheelTemperature (°C)",
    "CPUUsage (%)",
    "CPUTemperature (°C)",
    "SignalStrength (dBm)",
    "GyroMagnitude (deg/s)",
    "Altitude (km)"
]


class Predictor:

    def __init__(self):
        self.rf = joblib.load(RF_MODEL)
        self.xgb = joblib.load(XGB_MODEL)
        self.lstm = tf.keras.models.load_model(LSTM_MODEL)

    def _prepare(self, sample):

        if isinstance(sample, dict):
            sample = pd.DataFrame([sample])

        elif isinstance(sample, pd.Series):
            sample = sample.to_frame().T

        return sample[FEATURE_COLUMNS]

    def predict(self, sample, model="xgb"):

        sample = self._prepare(sample)

        model = model.lower()

        if model == "rf":
            return int(self.rf.predict(sample)[0])

        elif model == "xgb":
            return int(self.xgb.predict(sample)[0])

        elif model == "lstm":

            x = sample.values.reshape(1, 1, len(FEATURE_COLUMNS))

            pred = self.lstm.predict(x, verbose=0)

            return int(pred.argmax())

        else:
            raise ValueError("Model must be rf, xgb or lstm")


if __name__ == "__main__":

    from src.data.dataset import load_demo

    demo = load_demo()

    sample = demo.iloc[[0]]

    predictor = Predictor()

    print("Random Forest :", predictor.predict(sample, "rf"))
    print("XGBoost       :", predictor.predict(sample, "xgb"))