from pathlib import Path

import joblib
import shap
import pandas as pd
import matplotlib.pyplot as plt

from src.data.dataset import (
    load_test,
    split_features_target,
)


PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODEL_PATH = PROJECT_ROOT / "saved_models" / "xgboost.pkl"

REPORT_DIR = PROJECT_ROOT / "reports"
REPORT_DIR.mkdir(exist_ok=True)


def main():

    print("\nLoading Model...\n")

    model = joblib.load(MODEL_PATH)

    test = load_test()

    X_test, _ = split_features_target(test)

    sample = X_test.sample(
        min(500, len(X_test)),
        random_state=42,
    )

    explainer = shap.TreeExplainer(model)

    shap_values = explainer.shap_values(sample)

    plt.figure(figsize=(12, 8))

    shap.summary_plot(
        shap_values,
        sample,
        show=False,
    )

    plt.tight_layout()

    plt.savefig(
        REPORT_DIR / "shap_summary.png",
        dpi=300,
        bbox_inches="tight",
    )

    plt.close()

    plt.figure(figsize=(12, 8))

    shap.summary_plot(
        shap_values,
        sample,
        plot_type="bar",
        show=False,
    )

    plt.tight_layout()

    plt.savefig(
        REPORT_DIR / "shap_feature_importance.png",
        dpi=300,
        bbox_inches="tight",
    )

    plt.close()

    print("\nSHAP reports generated successfully.")
    print(f"\nReports saved to:\n{REPORT_DIR}")


if __name__ == "__main__":
    main()