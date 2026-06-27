from pathlib import Path
import joblib

from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from src.data.dataset import load_train, load_test, split_features_target

PROJECT_ROOT = Path(__file__).resolve().parents[2]
MODEL_PATH = PROJECT_ROOT / "saved_models" / "xgboost.pkl"

train = load_train()
test = load_test()

X_train, y_train = split_features_target(train)
X_test, y_test = split_features_target(test)

model = XGBClassifier(
    objective="multi:softmax",
    num_class=7,
    n_estimators=200,
    max_depth=8,
    learning_rate=0.1,
    random_state=42,
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print(f"\nAccuracy : {accuracy_score(y_test,pred):.4f}\n")

print(classification_report(y_test, pred, zero_division=0))

print(confusion_matrix(y_test, pred))

joblib.dump(model, MODEL_PATH)

print("\nModel Saved")