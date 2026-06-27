from pathlib import Path

import joblib
import pandas as pd
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODEL = PROJECT_ROOT / "saved_models" / "random_forest.pkl"
REPORTS = PROJECT_ROOT / "reports"

REPORTS.mkdir(exist_ok=True)

model = joblib.load(MODEL)

FEATURES = [
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

importance = pd.DataFrame({
    "Feature": FEATURES,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

importance.to_csv(
    REPORTS / "feature_importance.csv",
    index=False
)

plt.figure(figsize=(10,6))

plt.barh(
    importance["Feature"],
    importance["Importance"]
)

plt.gca().invert_yaxis()

plt.tight_layout()

plt.savefig(
    REPORTS / "feature_importance.png",
    dpi=300
)

plt.close()

print("Feature importance generated.")