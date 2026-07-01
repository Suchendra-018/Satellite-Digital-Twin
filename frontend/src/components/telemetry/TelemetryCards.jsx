import "./TelemetryCards.css";

function TelemetryCards({ data }) {
  if (!data?.telemetry) return null;

  const t = data.telemetry;

  const value = (key, digits = 2, unit = "") => {
    const v = t[key];

    if (v === undefined || v === null) {
      return "--";
    }

    if (typeof v === "number") {
      return `${v.toFixed(digits)}${unit}`;
    }

    return `${v}${unit}`;
  };

  const cards = [
    {
      title: "Bus Voltage",
      value: value("BusVoltage (V)", 2, " V"),
    },
    {
      title: "Battery Temp",
      value: value("BatteryTemperature (°C)", 1, " °C"),
    },
    {
      title: "Battery SOC",
      value: value("BatterySOC (%)", 1, " %"),
    },
    {
      title: "CPU Temp",
      value: value("CPUTemperature (°C)", 1, " °C"),
    },
    {
      title: "CPU Usage",
      value: value("CPUUsage (%)", 1, " %"),
    },
    {
      title: "Signal Strength",
      value: value("SignalStrength (dBm)", 0, " dBm"),
    },
    {
      title: "Wheel RPM",
      value: value("WheelRPM (RPM)", 0, " RPM"),
    },
    {
      title: "Altitude",
      value: value("Altitude (km)", 2, " km"),
    },
  ];

  return (
    <section className="telemetry-cards">
      {cards.map((card) => (
        <div className="telemetry-card" key={card.title}>
          <span>{card.title}</span>
          <h3>{card.value}</h3>
        </div>
      ))}
    </section>
  );
}

export default TelemetryCards;
