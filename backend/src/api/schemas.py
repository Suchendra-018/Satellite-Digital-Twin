from pydantic import BaseModel, Field


class ManualPredictionRequest(BaseModel):
    orbit_phase: float = Field(..., alias="OrbitPhase (%)")
    sunlight: float = Field(..., alias="Sunlight (0 or 1)")
    bus_voltage: float = Field(..., alias="BusVoltage (V)")
    bus_current: float = Field(..., alias="BusCurrent (A)")
    battery_voltage: float = Field(..., alias="BatteryVoltage (V)")
    battery_temperature: float = Field(..., alias="BatteryTemperature (°C)")
    battery_soc: float = Field(..., alias="BatterySOC (%)")
    solar_voltage: float = Field(..., alias="SolarVoltage (V)")
    solar_current: float = Field(..., alias="SolarCurrent (A)")
    wheel_rpm: float = Field(..., alias="WheelRPM (RPM)")
    wheel_temperature: float = Field(..., alias="WheelTemperature (°C)")
    cpu_usage: float = Field(..., alias="CPUUsage (%)")
    cpu_temperature: float = Field(..., alias="CPUTemperature (°C)")
    signal_strength: float = Field(..., alias="SignalStrength (dBm)")
    gyro_magnitude: float = Field(..., alias="GyroMagnitude (deg/s)")
    altitude: float = Field(..., alias="Altitude (km)")

    class Config:
        populate_by_name = True

    def to_model_input(self):
        return {
            "OrbitPhase (%)": self.orbit_phase,
            "Sunlight (0 or 1)": self.sunlight,
            "BusVoltage (V)": self.bus_voltage,
            "BusCurrent (A)": self.bus_current,
            "BatteryVoltage (V)": self.battery_voltage,
            "BatteryTemperature (°C)": self.battery_temperature,
            "BatterySOC (%)": self.battery_soc,
            "SolarVoltage (V)": self.solar_voltage,
            "SolarCurrent (A)": self.solar_current,
            "WheelRPM (RPM)": self.wheel_rpm,
            "WheelTemperature (°C)": self.wheel_temperature,
            "CPUUsage (%)": self.cpu_usage,
            "CPUTemperature (°C)": self.cpu_temperature,
            "SignalStrength (dBm)": self.signal_strength,
            "GyroMagnitude (deg/s)": self.gyro_magnitude,
            "Altitude (km)": self.altitude,
        }