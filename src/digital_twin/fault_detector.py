from pathlib import Path

from src.models.predictor import Predictor


class FaultDetector:

    FAULTS = {
        0: "Normal",
        1: "Power Anomaly",
        2: "Battery Degradation",
        3: "Reaction Wheel Fault",
        4: "Thermal Fault",
        5: "Communication Fault",
        6: "Sensor Fault",
    }

    def __init__(self, model="xgb"):
        self.model = model
        self.predictor = Predictor()

    def detect(self, telemetry):

        fault_id = self.predictor.predict(
            telemetry,
            self.model
        )

        return {
            "fault_id": fault_id,
            "fault_name": self.FAULTS[fault_id]
        }


if __name__ == "__main__":

    from src.digital_twin.simulator import SatelliteSimulator

    simulator = SatelliteSimulator()

    detector = FaultDetector()

    result = detector.detect(
        simulator.current_state()
    )

    print(result)