from pathlib import Path
import pandas as pd

# Project Paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATASET_PATH = PROJECT_ROOT / "datasets" / "train.csv"

# Required Columns
REQUIRED_COLUMNS = [
    "Timestamp (UTC)",
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
    "FaultLabel",
]


def load_dataset(path=DATASET_PATH):
    """Load telemetry dataset."""
    return pd.read_csv(path)


def validate_dataset(df):
    """Basic dataset validation."""

    missing_columns = [
        col for col in REQUIRED_COLUMNS if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(f"Missing Columns: {missing_columns}")

    if df.isnull().sum().sum() != 0:
        raise ValueError("Dataset contains missing values.")

    if df.duplicated().sum() != 0:
        raise ValueError("Dataset contains duplicate rows.")

    return True


def convert_timestamp(df):
    """Convert timestamp to datetime."""
    df["Timestamp (UTC)"] = pd.to_datetime(df["Timestamp (UTC)"])
    return df


def preprocess_data():
    """Complete preprocessing pipeline."""

    df = load_dataset()

    validate_dataset(df)

    df = convert_timestamp(df)

    return df


def main():
    df = preprocess_data()

    print("=" * 50)
    print("Satellite Telemetry Preprocessing")
    print("=" * 50)
    print(df.info())
    print()
    print(df.head())


if __name__ == "__main__":
    main()