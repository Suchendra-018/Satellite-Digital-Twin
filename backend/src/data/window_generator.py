from pathlib import Path

import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATASET_PATH = PROJECT_ROOT / "datasets" / "train_scaled.csv"

WINDOW_SIZE = 20

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


def load_dataset():
    return pd.read_csv(DATASET_PATH)


def create_windows(df):

    X = []
    y = []

    features = df[FEATURE_COLUMNS].values
    labels = df[TARGET].values

    for i in range(len(df) - WINDOW_SIZE):

        X.append(features[i:i + WINDOW_SIZE])
        y.append(labels[i + WINDOW_SIZE])

    return np.array(X), np.array(y)


def main():

    df = load_dataset()

    X, y = create_windows(df)

    print("X Shape :", X.shape)
    print("y Shape :", y.shape)

    print("\nExample Window Shape :", X[0].shape)
    print("Example Label :", y[0])


if __name__ == "__main__":
    main()