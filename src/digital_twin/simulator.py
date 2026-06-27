from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATASET = PROJECT_ROOT / "datasets" / "demo.csv"


class SatelliteSimulator:

    def __init__(self):
        self.df = pd.read_csv(DATASET)
        self.index = 0

    def reset(self):
        self.index = 0

    def current_state(self):

        return self.df.iloc[[self.index]]

    def next_state(self):

        if self.index < len(self.df) - 1:
            self.index += 1

        return self.current_state()

    def has_next(self):

        return self.index < len(self.df) - 1


if __name__ == "__main__":

    simulator = SatelliteSimulator()

    print("Current")

    print(simulator.current_state())

    print("\nNext")

    print(simulator.next_state())