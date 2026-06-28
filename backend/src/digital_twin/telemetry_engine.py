from src.data.dataset import load_demo


class TelemetryEngine:
    def __init__(self):
        self.data = load_demo()

    def latest(self):
        """
        Returns the latest telemetry sample.
        """
        return self.data.iloc[-1].to_dict()

    def all(self):
        """
        Returns the complete telemetry dataframe.
        """
        return self.data