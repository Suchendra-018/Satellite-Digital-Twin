from pathlib import Path

import joblib
import pandas as pd
from lime.lime_tabular import LimeTabularExplainer

from src.data.dataset import (
    FEATURE_COLUMNS,
    load_train,
)


PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODEL_PATH = PROJECT_ROOT / "saved_models" / "random_forest.pkl"
SCALER_PATH = PROJECT_ROOT / "saved_models" / "scaler.pkl"


CLASS_NAMES = [
    "Normal",
    "Battery Degradation",
    "Communication Fault",
    "Power Anomaly",
    "Reaction Wheel Fault",
    "Sensor Fault",
    "Thermal Fault",
]


class LIMEExplainer:

    def __init__(self):

        self.model = joblib.load(MODEL_PATH)
        self.scaler = joblib.load(SCALER_PATH)

        train = load_train()

        X_train = train[FEATURE_COLUMNS].copy()
        X_train[FEATURE_COLUMNS] = self.scaler.transform(
            X_train[FEATURE_COLUMNS]
        )

        self.explainer = LimeTabularExplainer(
            training_data=X_train.values,
            feature_names=FEATURE_COLUMNS,
            class_names=CLASS_NAMES,
            mode="classification",
            discretize_continuous=True,
        )

    def _prepare(self, sample):

        if isinstance(sample, dict):
            sample = pd.DataFrame([sample])

        elif isinstance(sample, pd.Series):
            sample = sample.to_frame().T

        sample = sample[FEATURE_COLUMNS].copy()

        for col in FEATURE_COLUMNS:
            sample[col] = pd.to_numeric(
                sample[col],
                errors="coerce",
            )

        return sample.astype(float)

    def _scale(self, sample):

        sample = sample.copy()

        sample[FEATURE_COLUMNS] = self.scaler.transform(
            sample[FEATURE_COLUMNS]
        )

        return sample

    def explain(self, sample):

        sample = self._prepare(sample)
        sample = self._scale(sample)

        explanation = self.explainer.explain_instance(
            sample.iloc[0].values,
            self.model.predict_proba,
            num_features=10,
        )

        features = []

        for feature, weight in explanation.as_list():

            features.append(
                {
                    "feature": feature,
                    "impact": round(float(weight), 5),
                }
            )

        prediction = int(self.model.predict(sample)[0])

        return {
            "prediction": prediction,
            "prediction_name": CLASS_NAMES[prediction],
            "top_features": features,
        }


lime_explainer = LIMEExplainer()


if __name__ == "__main__":

    from src.data.dataset import load_demo_original

    sample = load_demo_original().iloc[[0]]

    result = lime_explainer.explain(sample)

    print("\nPrediction")
    print(result["prediction_name"])

    print("\nTop LIME Features\n")

    for item in result["top_features"]:
        print(item)