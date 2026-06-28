from pathlib import Path
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from src.data.dataset import (
    load_train,
    load_test,
    split_features_target,
)

PROJECT_ROOT = Path(__file__).resolve().parents[2]
MODEL_PATH = PROJECT_ROOT / "saved_models" / "random_forest.pkl"


def train_model():
    train_df = load_train()
    test_df = load_test()

    X_train, y_train = split_features_target(train_df)
    X_test, y_test = split_features_target(test_df)

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print(f"\nAccuracy : {accuracy:.4f}\n")

    print("Classification Report\n")
    print(classification_report(y_test, predictions))

    print("Confusion Matrix\n")
    print(confusion_matrix(y_test, predictions))

    joblib.dump(model, MODEL_PATH)

    print(f"\nModel saved to:\n{MODEL_PATH}")


if __name__ == "__main__":
    train_model()