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
    objective="multi:softprob",
    num_class=7,
    eval_metric="mlogloss",

    n_estimators=500,
    learning_rate=0.05,
    max_depth=10,

    min_child_weight=2,
    gamma=0.2,

    subsample=0.9,
    colsample_bytree=0.9,

    reg_alpha=0.2,
    reg_lambda=2.0,

    random_state=42,
    tree_method="hist",
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print(f"\nAccuracy : {accuracy_score(y_test,pred):.4f}\n")

print(classification_report(y_test, pred, zero_division=0))

print(confusion_matrix(y_test, pred))

joblib.dump(model, MODEL_PATH)

print("\nModel Saved")