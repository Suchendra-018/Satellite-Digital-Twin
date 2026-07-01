const API_BASE = "http://127.0.0.1:8000/api";

export async function predictFault(data) {
  const response = await fetch(`${API_BASE}/predict/manual`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  if (!response.ok) {
    throw new Error("Prediction failed.");
  }

  return await response.json();
}

const random = (min, max, decimals = 2) =>
  Number((Math.random() * (max - min) + min).toFixed(decimals));

export function emptyTelemetry() {
  return {
    "OrbitPhase (%)": "",
    "Sunlight (0 or 1)": "",

    "BusVoltage (V)": "",
    "BusCurrent (A)": "",

    "BatteryVoltage (V)": "",
    "BatteryTemperature (°C)": "",
    "BatterySOC (%)": "",

    "SolarVoltage (V)": "",
    "SolarCurrent (A)": "",

    "WheelRPM (RPM)": "",
    "WheelTemperature (°C)": "",

    "CPUUsage (%)": "",
    "CPUTemperature (°C)": "",

    "SignalStrength (dBm)": "",

    "GyroMagnitude (deg/s)": "",

    "Altitude (km)": "",
  };
}
export function generateHealthyTelemetry() {
  const telemetry = {
    ...NORMAL_SAMPLES[Math.floor(Math.random() * NORMAL_SAMPLES.length)],
  };

  return {
    scenario: "Normal",
    telemetry,
  };
}

const NORMAL_SAMPLES = [
  {
    "OrbitPhase (%)": 45,
    "Sunlight (0 or 1)": 1,
    "BusVoltage (V)": 32.0,
    "BusCurrent (A)": 3.1,
    "BatteryVoltage (V)": 7.9,
    "BatteryTemperature (°C)": 25,
    "BatterySOC (%)": 96,
    "SolarVoltage (V)": 9.1,
    "SolarCurrent (A)": 1.8,
    "WheelRPM (RPM)": 950,
    "WheelTemperature (°C)": 30,
    "CPUUsage (%)": 36,
    "CPUTemperature (°C)": 42,
    "SignalStrength (dBm)": -74,
    "GyroMagnitude (deg/s)": 0.022,
    "Altitude (km)": 550,
  },
  {
    "OrbitPhase (%)": 58,
    "Sunlight (0 or 1)": 1,
    "BusVoltage (V)": 31.9,
    "BusCurrent (A)": 3.0,
    "BatteryVoltage (V)": 7.8,
    "BatteryTemperature (°C)": 24,
    "BatterySOC (%)": 94,
    "SolarVoltage (V)": 8.9,
    "SolarCurrent (A)": 1.7,
    "WheelRPM (RPM)": 1000,
    "WheelTemperature (°C)": 31,
    "CPUUsage (%)": 40,
    "CPUTemperature (°C)": 43,
    "SignalStrength (dBm)": -75,
    "GyroMagnitude (deg/s)": 0.024,
    "Altitude (km)": 551,
  },
  {
    "OrbitPhase (%)": 63,
    "Sunlight (0 or 1)": 1,
    "BusVoltage (V)": 32.1,
    "BusCurrent (A)": 3.2,
    "BatteryVoltage (V)": 7.9,
    "BatteryTemperature (°C)": 26,
    "BatterySOC (%)": 98,
    "SolarVoltage (V)": 9.0,
    "SolarCurrent (A)": 1.9,
    "WheelRPM (RPM)": 920,
    "WheelTemperature (°C)": 29,
    "CPUUsage (%)": 34,
    "CPUTemperature (°C)": 41,
    "SignalStrength (dBm)": -73,
    "GyroMagnitude (deg/s)": 0.021,
    "Altitude (km)": 549,
  },
  {
    "OrbitPhase (%)": 51,
    "Sunlight (0 or 1)": 1,
    "BusVoltage (V)": 32.0,
    "BusCurrent (A)": 3.3,
    "BatteryVoltage (V)": 7.8,
    "BatteryTemperature (°C)": 24,
    "BatterySOC (%)": 97,
    "SolarVoltage (V)": 9.2,
    "SolarCurrent (A)": 2.0,
    "WheelRPM (RPM)": 980,
    "WheelTemperature (°C)": 31,
    "CPUUsage (%)": 35,
    "CPUTemperature (°C)": 42,
    "SignalStrength (dBm)": -74,
    "GyroMagnitude (deg/s)": 0.023,
    "Altitude (km)": 552,
  },
  {
    "OrbitPhase (%)": 38,
    "Sunlight (0 or 1)": 1,
    "BusVoltage (V)": 31.9,
    "BusCurrent (A)": 3.0,
    "BatteryVoltage (V)": 7.9,
    "BatteryTemperature (°C)": 25,
    "BatterySOC (%)": 95,
    "SolarVoltage (V)": 8.8,
    "SolarCurrent (A)": 1.8,
    "WheelRPM (RPM)": 970,
    "WheelTemperature (°C)": 30,
    "CPUUsage (%)": 38,
    "CPUTemperature (°C)": 43,
    "SignalStrength (dBm)": -76,
    "GyroMagnitude (deg/s)": 0.025,
    "Altitude (km)": 550,
  },
  {
    "OrbitPhase (%)": 60,
    "Sunlight (0 or 1)": 1,
    "BusVoltage (V)": 32.0,
    "BusCurrent (A)": 3.2,
    "BatteryVoltage (V)": 7.8,
    "BatteryTemperature (°C)": 26,
    "BatterySOC (%)": 94,
    "SolarVoltage (V)": 9.0,
    "SolarCurrent (A)": 1.9,
    "WheelRPM (RPM)": 940,
    "WheelTemperature (°C)": 30,
    "CPUUsage (%)": 37,
    "CPUTemperature (°C)": 42,
    "SignalStrength (dBm)": -74,
    "GyroMagnitude (deg/s)": 0.022,
    "Altitude (km)": 551,
  },
];

export function generateFaultScenario() {
  const telemetry = {
    ...NORMAL_SAMPLES[Math.floor(Math.random() * NORMAL_SAMPLES.length)],
  };

  const faults = [
    "Battery Degradation",
    "Communication Fault",
    "Power Anomaly",
    "Reaction Wheel Fault",
    "Thermal Fault",
    "Sensor Fault",
  ];

  const scenario = faults[Math.floor(Math.random() * faults.length)];

  switch (scenario) {
    case "Battery Degradation":
      telemetry["BatteryVoltage (V)"] = random(6.4, 6.9);
      telemetry["BatterySOC (%)"] = random(5, 25);
      telemetry["BatteryTemperature (°C)"] = random(45, 60);
      break;

    case "Communication Fault":
      telemetry["SignalStrength (dBm)"] = random(-118, -108);
      break;

    case "Power Anomaly":
      telemetry["BusVoltage (V)"] = random(27.5, 29.0);
      telemetry["BusCurrent (A)"] = random(8, 12);
      telemetry["SolarVoltage (V)"] = random(0.5, 3);
      telemetry["SolarCurrent (A)"] = random(0, 0.4);
      break;

    case "Reaction Wheel Fault":
      telemetry["WheelRPM (RPM)"] = random(6000, 7800);
      telemetry["WheelTemperature (°C)"] = random(60, 80);
      telemetry["GyroMagnitude (deg/s)"] = random(2, 4);
      break;

    case "Thermal Fault":
      telemetry["BatteryTemperature (°C)"] = random(60, 75);
      telemetry["CPUTemperature (°C)"] = random(75, 90);
      telemetry["WheelTemperature (°C)"] = random(65, 80);
      break;

    case "Sensor Fault":
      telemetry["GyroMagnitude (deg/s)"] = random(3, 5);
      telemetry["CPUUsage (%)"] = random(80, 100);
      break;

    case "Normal":
    default:
      break;
  }

  return {
    scenario,
    telemetry,
  };
}