import time

from src.digital_twin.simulator import SatelliteSimulator
from src.digital_twin.fault_detector import FaultDetector


class DigitalTwin:

    def __init__(self):

        self.simulator = SatelliteSimulator()
        self.detector = FaultDetector()

    def run(self, steps=20, delay=0.5):

     print("\n===== Satellite Digital Twin Started =====\n")

     count = 0

     while self.simulator.has_next() and count < steps:

        telemetry = self.simulator.current_state()

        result = self.detector.detect(telemetry)

        print(
            f"{telemetry['Timestamp (UTC)'].iloc[0]} | "
            f"Prediction: {result['fault_name']}"
        )

        self.simulator.next_state()

        count += 1

        time.sleep(delay)

    print("\n===== Simulation Finished =====")


if __name__ == "__main__":

    twin = DigitalTwin()

    twin.run(steps=20, delay=0.1)