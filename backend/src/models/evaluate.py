from pathlib import Path
import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report,
)

from src.data.dataset import load_test, split_features_target

PROJECT_ROOT = Path(__file__).resolve().parents[2]

REPORT_DIR = PROJECT_ROOT / "reports"
REPORT_DIR.mkdir(exist_ok=True)

RF_MODEL = PROJECT_ROOT / "saved_models" / "random_forest.pkl"
XGB_MODEL = PROJECT_ROOT / "saved_models" / "xgboost.pkl"

test = load_test()
X_test, y_test = split_features_target(test)

results = []


def evaluate(model_name, model, image_name):
    pred = model.predict(X_test)

    # Overall metrics
    results.append({
        "Model": model_name,
        "Accuracy": accuracy_score(y_test, pred),
        "Precision": precision_score(
            y_test, pred, average="weighted", zero_division=0
        ),
        "Recall": recall_score(
            y_test, pred, average="weighted", zero_division=0
        ),
        "F1 Score": f1_score(
            y_test, pred, average="weighted", zero_division=0
        ),
    })

    # Classification Report
    report = classification_report(
        y_test,
        pred,
        output_dict=True,
        zero_division=0,
    )

    report_df = pd.DataFrame(report).transpose()

    report_df.to_csv(
        REPORT_DIR / f"{model_name.lower().replace(' ', '_')}_classification_report.csv",
        index=True,
    )

    # Confusion Matrix
    cm = confusion_matrix(y_test, pred)

    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot(cmap="Blues")

    plt.title(model_name)

    plt.savefig(
        REPORT_DIR / image_name,
        dpi=300,
        bbox_inches="tight",
    )

    plt.close()


# -------------------------
# Evaluate Random Forest
# -------------------------
rf = joblib.load(RF_MODEL)
evaluate(
    "Random Forest",
    rf,
    "confusion_matrix_rf.png",
)

# -------------------------
# Evaluate XGBoost
# -------------------------
xgb = joblib.load(XGB_MODEL)
evaluate(
    "XGBoost",
    xgb,
    "confusion_matrix_xgb.png",
)

# Save overall model results
results_df = pd.DataFrame(results)

results_df.to_csv(
    REPORT_DIR / "model_results.csv",
    index=False,
)

# Random Forest Feature Importance
importance = pd.DataFrame({
    "Feature": X_test.columns,
    "Importance": rf.feature_importances_,
})

importance.sort_values(
    by="Importance",
    ascending=False,
    inplace=True,
)

importance.to_csv(
    REPORT_DIR / "feature_importance.csv",
    index=False,
)

print(results_df)
print("\nReports Generated Successfully")