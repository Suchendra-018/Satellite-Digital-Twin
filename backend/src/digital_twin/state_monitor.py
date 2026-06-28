from src.digital_twin.simulator import SatelliteSimulator
from src.digital_twin.fault_detector import FaultDetector


class StateMonitor:

    def __init__(self):
        self.simulator = SatelliteSimulator()
        self.detector = FaultDetector()

    def monitor_once(self):

        telemetry = self.simulator.current_state()

        prediction = self.detector.detect(telemetry)

        return {
            "timestamp": telemetry["Timestamp (UTC)"].iloc[0],
            "fault_id": prediction["fault_id"],
            "fault_name": prediction["fault_name"],
        }


if __name__ == "__main__":

    monitor = StateMonitor()

    print(monitor.monitor_once())