from pathlib import Path

import joblib

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)

from xgboost import XGBClassifier

from src.data.dataset import (
    load_train,
    load_test,
    split_features_target,
)


PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODEL_PATH = PROJECT_ROOT / "saved_models" / "xgboost.pkl"


def main():

    print("\nLoading Dataset...\n")

    train = load_train()
    test = load_test()

    X_train, y_train = split_features_target(train)
    X_test, y_test = split_features_target(test)

    model = XGBClassifier(

        objective="multi:softprob",
        num_class=7,

        eval_metric="mlogloss",

        n_estimators=800,
        learning_rate=0.03,
        max_depth=8,

        min_child_weight=2,
        gamma=0.15,

        subsample=0.90,
        colsample_bytree=0.90,

        reg_alpha=0.10,
        reg_lambda=1.50,

        random_state=42,

        tree_method="hist",

        n_jobs=-1,
    )

    print("Training XGBoost...\n")

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
    main()