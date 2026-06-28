from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATASET_DIR = PROJECT_ROOT / "datasets"


def load_train():
    return pd.read_csv(
        DATASET_DIR / "train_scaled.csv",
        low_memory=False
    )


def load_test():
    return pd.read_csv(
        DATASET_DIR / "test_scaled.csv",
        low_memory=False
    )


def load_demo():
    return pd.read_csv(
        DATASET_DIR / "demo_scaled.csv",
        low_memory=False
    )


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
    "Altitude (km)",
]

TARGET_COLUMN = "FaultLabel"


def split_features_target(df):
    X = df[FEATURE_COLUMNS]
    y = df[TARGET_COLUMN]
    return X, y


if __name__ == "__main__":

    train = load_train()
    test = load_test()

    X_train, y_train = split_features_target(train)
    X_test, y_test = split_features_target(test)

    print("Train:", X_train.shape, y_train.shape)
    print("Test :", X_test.shape, y_test.shape)