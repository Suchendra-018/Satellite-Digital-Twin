from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import shap

from src.data.dataset import FEATURE_COLUMNS

PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODEL_PATH = PROJECT_ROOT / "saved_models" / "xgboost.pkl"
SCALER_PATH = PROJECT_ROOT / "saved_models" / "scaler.pkl"


class SHAPExplainer:
    """
    Generates SHAP explanations for a single telemetry sample.
    """

    def __init__(self):

        self.model = joblib.load(MODEL_PATH)

        self.scaler = joblib.load(SCALER_PATH)

        self.explainer = shap.TreeExplainer(self.model)

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

        prediction = int(
            self.model.predict(sample)[0]
        )

        shap_values = self.explainer.shap_values(sample)

        # -----------------------------
        # Handle different SHAP versions
        # -----------------------------

        if isinstance(shap_values, list):

            values = np.array(shap_values[prediction][0])

        elif isinstance(shap_values, np.ndarray):

            if shap_values.ndim == 3:

                # (samples, features, classes)
                values = shap_values[0, :, prediction]

            elif shap_values.ndim == 2:

                values = shap_values[0]

            else:

                values = shap_values.flatten()

        else:

            values = np.array(shap_values).flatten()

        feature_importance = []

        for feature, value in zip(
            FEATURE_COLUMNS,
            values,
        ):

            feature_importance.append(
                {
                    "feature": feature,
                    "impact": round(float(value), 5),
                    "absolute_impact": round(abs(float(value)), 5),
                }
            )

        feature_importance.sort(
            key=lambda x: x["absolute_impact"],
            reverse=True,
        )

        return {
            "prediction": prediction,
            "top_features": feature_importance[:10],
            "all_features": feature_importance,
        }


shap_explainer = SHAPExplainer()


if __name__ == "__main__":

    from src.data.dataset import load_demo_original

    sample = load_demo_original().iloc[[0]]

    explanation = shap_explainer.explain(sample)

    print("\nPrediction:", explanation["prediction"])

    print("\nTop SHAP Features\n")

    for item in explanation["top_features"]:

        print(
            f"{item['feature']:<35}"
            f"{item['impact']:>10}"
        )