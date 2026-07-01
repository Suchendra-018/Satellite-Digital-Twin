from pathlib import Path

import joblib
import pandas as pd
import shap

from src.data.dataset import (
    FEATURE_COLUMNS,
)


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

        shap_values = self.explainer.shap_values(sample)

        if isinstance(shap_values, list):
            shap_values = shap_values[0]

        feature_importance = []

        for feature, value in zip(
            FEATURE_COLUMNS,
            shap_values[0],
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
            "top_features": feature_importance[:10],
            "all_features": feature_importance,
        }


shap_explainer = SHAPExplainer()


if __name__ == "__main__":

    from src.data.dataset import load_demo_original

    sample = load_demo_original().iloc[[0]]

    explanation = shap_explainer.explain(sample)

    print("\nTop SHAP Features\n")

    for item in explanation["top_features"]:
        print(
            f"{item['feature']:<35}"
            f"{item['impact']:>10}"
        )