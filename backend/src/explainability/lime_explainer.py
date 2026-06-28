from pathlib import Path

import joblib
import pandas as pd

from lime.lime_tabular import LimeTabularExplainer

from src.data.dataset import load_train, load_test, split_features_target

PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODEL = PROJECT_ROOT / "saved_models" / "random_forest.pkl"
REPORTS = PROJECT_ROOT / "reports"

REPORTS.mkdir(exist_ok=True)

model = joblib.load(MODEL)

train = load_train()
test = load_test()

X_train, y_train = split_features_target(train)
X_test, y_test = split_features_target(test)

explainer = LimeTabularExplainer(
    training_data=X_train.values,
    feature_names=X_train.columns.tolist(),
    class_names=[str(i) for i in sorted(y_train.unique())],
    mode="classification"
)

exp = explainer.explain_instance(
    X_test.iloc[0].values,
    model.predict_proba,
    num_features=10
)

exp.save_to_file(REPORTS / "lime_explanation.html")

print("LIME report generated.")