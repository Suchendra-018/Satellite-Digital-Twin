from pathlib import Path

import joblib
import pandas as pd
import matplotlib.pyplot as plt


PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODEL_PATH = PROJECT_ROOT / "saved_models" / "random_forest.pkl"

REPORT_DIR = PROJECT_ROOT / "reports"
REPORT_DIR.mkdir(exist_ok=True)


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


def main():

    print("\nLoading Random Forest Model...\n")

    model = joblib.load(MODEL_PATH)

    importance = pd.DataFrame(
        {
            "Feature": FEATURE_COLUMNS,
            "Importance": model.feature_importances_,
        }
    )

    importance = importance.sort_values(
        by="Importance",
        ascending=False,
    )

    importance.to_csv(
        REPORT_DIR / "feature_importance.csv",
        index=False,
    )

    plt.figure(figsize=(12, 7))

    plt.barh(
        importance["Feature"],
        importance["Importance"],
    )

    plt.gca().invert_yaxis()

    plt.xlabel("Importance Score")
    plt.ylabel("Telemetry Features")
    plt.title("Random Forest Feature Importance")

    plt.grid(
        axis="x",
        linestyle="--",
        alpha=0.30,
    )

    plt.tight_layout()

    plt.savefig(
        REPORT_DIR / "feature_importance.png",
        dpi=300,
    )

    plt.close()

    print("\nTop 10 Important Features\n")
    print(importance.head(10))

    print(f"\nReports saved to:\n{REPORT_DIR}")


if __name__ == "__main__":
    main()