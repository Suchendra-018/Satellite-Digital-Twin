from pathlib import Path

import pandas as pd
from imblearn.combine import SMOTEENN
from imblearn.over_sampling import SMOTE

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATASET_DIR = PROJECT_ROOT / "datasets"

TRAIN_PATH = DATASET_DIR / "train.csv"
OUTPUT_PATH = DATASET_DIR / "train_balanced.csv"

FEATURE_COLUMNS = [
    "OrbitPhase (%)",
    "Sunlight (0 or 1)",
    "BusVoltage (V)",
    "BusCurrent (A)",
    "BatteryVoltage (V)",
    "BatteryTemperature (°C)",
    "BatterySOC (%)",
    "SolarVoltage (V)",
    "SolarCurrent (A)",
    "WheelRPM (RPM)",
    "WheelTemperature (°C)",
    "CPUUsage (%)",
    "CPUTemperature (°C)",
    "SignalStrength (dBm)",
    "GyroMagnitude (deg/s)",
    "Altitude (km)"
]

TARGET = "FaultLabel"

df = pd.read_csv(TRAIN_PATH)

print("\nOriginal Distribution")
print(df[TARGET].value_counts().sort_index())

metadata = df.drop(columns=FEATURE_COLUMNS + [TARGET])
X = df[FEATURE_COLUMNS]
y = df[TARGET]

smote = SMOTE(
    sampling_strategy="not majority",
    random_state=42,
    k_neighbors=5,
)

X_res, y_res = smote.fit_resample(X, y)

metadata = metadata.iloc[:len(X_res)].reset_index(drop=True)

balanced = pd.concat(
    [
        metadata,
        pd.DataFrame(X_res, columns=FEATURE_COLUMNS),
        pd.Series(y_res, name=TARGET),
    ],
    axis=1,
)

balanced.to_csv(OUTPUT_PATH, index=False)

print("\nBalanced Distribution")
print(balanced[TARGET].value_counts().sort_index())

print(f"\nSaved to:\n{OUTPUT_PATH}")