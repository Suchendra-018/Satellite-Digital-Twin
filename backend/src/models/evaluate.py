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


def evaluate_model(model_name, model, X_test, y_test):

    prediction = model.predict(X_test)

    metrics = {
        "Model": model_name,
        "Accuracy": round(
            accuracy_score(y_test, prediction),
            4,
        ),
        "Precision": round(
            precision_score(
                y_test,
                prediction,
                average="weighted",
                zero_division=0,
            ),
            4,
        ),
        "Recall": round(
            recall_score(
                y_test,
                prediction,
                average="weighted",
                zero_division=0,
            ),
            4,
        ),
        "F1 Score": round(
            f1_score(
                y_test,
                prediction,
                average="weighted",
                zero_division=0,
            ),
            4,
        ),
    }

    report = classification_report(
        y_test,
        prediction,
        output_dict=True,
        zero_division=0,
    )

    report_df = pd.DataFrame(report).transpose()

    report_df.to_csv(
        REPORT_DIR
        / f"{model_name.lower().replace(' ','_')}_classification_report.csv",
    )

    cm = confusion_matrix(
        y_test,
        prediction,
    )

    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm,
    )

    disp.plot(
        cmap="Blues",
        colorbar=False,
    )

    plt.title(f"{model_name} Confusion Matrix")

    plt.tight_layout()

    plt.savefig(
        REPORT_DIR
        / f"{model_name.lower().replace(' ','_')}_confusion_matrix.png",
        dpi=300,
    )

    plt.close()

    if hasattr(model, "feature_importances_"):

        importance = pd.DataFrame(
            {
                "Feature": X_test.columns,
                "Importance": model.feature_importances_,
            }
        )

        importance = importance.sort_values(
            "Importance",
            ascending=False,
        )

        importance.to_csv(
            REPORT_DIR
            / f"{model_name.lower().replace(' ','_')}_feature_importance.csv",
            index=False,
        )

    return metrics


def main():

    print("\nLoading Test Dataset...\n")

    test = load_test()

    X_test, y_test = split_features_target(test)

    rf = joblib.load(RF_MODEL)
    xgb = joblib.load(XGB_MODEL)

    results = []

    results.append(
        evaluate_model(
            "Random Forest",
            rf,
            X_test,
            y_test,
        )
    )

    results.append(
        evaluate_model(
            "XGBoost",
            xgb,
            X_test,
            y_test,
        )
    )

    results_df = pd.DataFrame(results)

    results_df.to_csv(
        REPORT_DIR / "model_results.csv",
        index=False,
    )

    print("\n============================")
    print(results_df)
    print("============================")

    print(f"\nReports saved to:\n{REPORT_DIR}")


if __name__ == "__main__":
    main()