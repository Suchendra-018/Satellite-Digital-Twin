from pathlib import Path

import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)

from src.data.dataset import (
    load_train,
    load_test,
    split_features_target,
)


PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODEL_PATH = PROJECT_ROOT / "saved_models" / "random_forest.pkl"


def train_model():

    print("\nLoading Dataset...\n")

    train_df = load_train()
    test_df = load_test()

    X_train, y_train = split_features_target(train_df)
    X_test, y_test = split_features_target(test_df)

    model = RandomForestClassifier(

        n_estimators=500,

        max_depth=20,

        min_samples_split=2,
        min_samples_leaf=1,

        max_features="sqrt",

        bootstrap=True,

        random_state=42,

        n_jobs=-1,
    )

    print("Training Random Forest...\n")

    model.fit(
        X_train,
        y_train,
    )

    prediction = model.predict(X_test)

    print("\n==============================")
    print(f"Accuracy : {accuracy_score(y_test, prediction):.4f}")
    print("==============================\n")

    print(
        classification_report(
            y_test,
            prediction,
            zero_division=0,
        )
    )

    print("\nConfusion Matrix\n")

    print(
        confusion_matrix(
            y_test,
            prediction,
        )
    )

    joblib.dump(
        model,
        MODEL_PATH,
    )

    print(f"\nModel Saved -> {MODEL_PATH}")


if __name__ == "__main__":
    train_model()