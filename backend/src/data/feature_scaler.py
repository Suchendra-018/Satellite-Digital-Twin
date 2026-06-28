from pathlib import Path

import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Project Paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATASET_DIR = PROJECT_ROOT / "datasets"
MODEL_DIR = PROJECT_ROOT / "saved_models"

TRAIN_PATH = DATASET_DIR / "train.csv"
TEST_PATH = DATASET_DIR / "test.csv"
DEMO_PATH = DATASET_DIR / "demo.csv"

SCALER_PATH = MODEL_DIR / "scaler.pkl"

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


def load_dataset(path):
    return pd.read_csv(path, low_memory=False)


def fit_scaler(train_df):
    scaler = StandardScaler()
    scaler.fit(train_df[FEATURE_COLUMNS])
    return scaler


def transform_dataset(df, scaler):
    df = df.copy()
    df[FEATURE_COLUMNS] = scaler.transform(df[FEATURE_COLUMNS])
    return df


def save_scaler(scaler):
    MODEL_DIR.mkdir(exist_ok=True)
    joblib.dump(scaler, SCALER_PATH)


def main():

    train_df = load_dataset(TRAIN_PATH)
    test_df = load_dataset(TEST_PATH)
    demo_df = load_dataset(DEMO_PATH)

    scaler = fit_scaler(train_df)

    train_scaled = transform_dataset(train_df, scaler)
    test_scaled = transform_dataset(test_df, scaler)
    demo_scaled = transform_dataset(demo_df, scaler)

    # Save scaled datasets
    train_scaled.to_csv(DATASET_DIR / "train_scaled.csv", index=False)
    test_scaled.to_csv(DATASET_DIR / "test_scaled.csv", index=False)
    demo_scaled.to_csv(DATASET_DIR / "demo_scaled.csv", index=False)

    save_scaler(scaler)

    print("\nTrain Shape :", train_scaled.shape)
    print("Test Shape  :", test_scaled.shape)
    print("Demo Shape  :", demo_scaled.shape)

    print("\nScaler saved to:")
    print(SCALER_PATH)

    print("\nScaled Feature Means")
    print(train_scaled[FEATURE_COLUMNS].mean().round(4))

    print("\nScaled Feature Std")
    print(train_scaled[FEATURE_COLUMNS].std().round(4))


if __name__ == "__main__":
    main()