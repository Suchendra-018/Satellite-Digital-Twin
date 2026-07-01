from pathlib import Path
import random

import pandas as pd

from src.data.dataset import FEATURE_COLUMNS


PROJECT_ROOT = Path(__file__).resolve().parents[3]

DATASET_PATH = PROJECT_ROOT / "datasets" / "demo.csv"


class ScenarioService:

    def __init__(self):
        self.demo = pd.read_csv(DATASET_PATH)

    def _telemetry(self, row):
        return {
            feature: float(row[feature])
            for feature in FEATURE_COLUMNS
        }

    def normal(self):
        normal = self.demo[
            self.demo["FaultLabel"] == 0
        ]
        print(normal[["FaultLabel"]].head())
        row = normal.sample(1).iloc[0]

        return {
            "scenario": "Normal",
            "telemetry": self._telemetry(row),
        }

    def fault(self):
        faults = self.demo[
            self.demo["FaultLabel"] != 0
        ]

        row = faults.sample(1).iloc[0]

        labels = {
            1: "Battery Degradation",
            2: "Communication Fault",
            3: "Power Anomaly",
            4: "Reaction Wheel Fault",
            5: "Sensor Fault",
            6: "Thermal Fault",
        }

        return {
            "scenario": labels.get(
                int(row["FaultLabel"]),
                "Unknown",
            ),
            "telemetry": self._telemetry(row),
        }


scenario_service = ScenarioService()