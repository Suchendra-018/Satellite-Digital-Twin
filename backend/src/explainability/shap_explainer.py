from pathlib import Path

import joblib
import pandas as pd
import shap
import matplotlib.pyplot as plt

from src.data.dataset import load_test, split_features_target

PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODEL = PROJECT_ROOT / "saved_models" / "random_forest.pkl"
REPORTS = PROJECT_ROOT / "reports"

REPORTS.mkdir(exist_ok=True)

model = joblib.load(MODEL)

test = load_test()

X_test, y_test = split_features_target(test)

sample = X_test.sample(500, random_state=42)

explainer = shap.TreeExplainer(model)

shap_values = explainer.shap_values(sample)

plt.figure()

shap.summary_plot(
    shap_values,
    sample,
    show=False
)

plt.savefig(
    REPORTS / "shap_summary.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("SHAP report generated.")
