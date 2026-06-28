import time
from pathlib import Path

import pandas as pd

from src.digital_twin.simulator import SatelliteSimulator
from src.digital_twin.fault_detector import FaultDetector
from src.models.predictor import Predictor


PROJECT_ROOT = Path(__file__).resolve().parents[2]

REPORT_DIR = PROJECT_ROOT / "reports"
REPORT_DIR.mkdir(exist_ok=True)


class DigitalTwin:

    HEALTH_SCORE = {
        "Normal": 100,
        "Power Anomaly": 80,
        "Battery Degradation": 75,
        "Reaction Wheel Fault": 70,
        "Thermal Fault": 65,
        "Communication Fault": 60,
        "Sensor Fault": 85,
    }

    ALERT_LEVEL = {
        "Normal": "NORMAL",
        "Power Anomaly": "WARNING",
        "Battery Degradation": "WARNING",
        "Reaction Wheel Fault": "CRITICAL",
        "Thermal Fault": "CRITICAL",
        "Communication Fault": "WARNING",
        "Sensor Fault": "WARNING",
    }

    def __init__(self):

        self.simulator = SatelliteSimulator()
        self.detector = FaultDetector(model="xgb")
        self.predictor = Predictor()

        self.logs = []

    def run(self, delay=0.0):

        print("\n========== SATELLITE DIGITAL TWIN ==========\n")

        while True:

            telemetry = self.simulator.current_state()

            result = self.detector.detect(telemetry)

            probabilities = self.predictor.xgb.predict_proba(
                self.predictor._prepare(telemetry)
            )[0]

            confidence = round(probabilities.max() * 100, 2)

            timestamp = telemetry["Timestamp (UTC)"].iloc[0]

            prediction = result["fault_name"]

            health = self.HEALTH_SCORE[prediction]

            alert = self.ALERT_LEVEL[prediction]

            row = {
                "Timestamp": timestamp,
                "Prediction": prediction,
                "Confidence": confidence,
                "HealthScore": health,
                "Alert": alert,
                "OrbitPhase": telemetry["OrbitPhase (%)"].iloc[0],
                "BusVoltage": telemetry["BusVoltage (V)"].iloc[0],
                "BatterySOC": telemetry["BatterySOC (%)"].iloc[0],
                "BatteryTemp": telemetry["BatteryTemperature (°C)"].iloc[0],
                "WheelRPM": telemetry["WheelRPM (RPM)"].iloc[0],
                "CPUUsage": telemetry["CPUUsage (%)"].iloc[0],
                "SignalStrength": telemetry["SignalStrength (dBm)"].iloc[0],
            }

            self.logs.append(row)

            print(
                f"{timestamp} | "
                f"{prediction:<24} | "
                f"{confidence:6.2f}% | "
                f"Health {health:3d} | "
                f"{alert}"
            )

            if not self.simulator.has_next():
                break

            self.simulator.next_state()

            if delay > 0:
                time.sleep(delay)

        df = pd.DataFrame(self.logs)

        output = REPORT_DIR / "digital_twin_log.csv"

        df.to_csv(output, index=False)

        print("\n========================================")
        print("Simulation Completed")
        print(f"Samples : {len(df)}")
        print(f"Output  : {output}")
        print("========================================")


if __name__ == "__main__":

    DigitalTwin().run(delay=0.0)