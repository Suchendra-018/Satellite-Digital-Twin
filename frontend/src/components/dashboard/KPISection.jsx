import "./KPISection.css";

import {
  FaHeartbeat,
  FaExclamationTriangle,
  FaSatellite,
} from "react-icons/fa";

import { MdOutlinePsychology } from "react-icons/md";

function KPISection({ data }) {
  if (!data?.telemetry) return null;

  const telemetry = data.telemetry;

  const prediction =
    typeof data.prediction === "string"
      ? data.prediction
      : (data.prediction?.fault_name ??
        data.prediction?.prediction ??
        "Unknown");

  const cards = [
    {
      title: "Battery Voltage",
      value: `${Number(telemetry["BatteryVoltage (V)"] ?? 0).toFixed(3)} V`,
      icon: <FaHeartbeat />,
      color: "#22c55e",
    },
    {
      title: "Battery Temperature",
      value: `${Number(telemetry["BatteryTemperature (°C)"] ?? 0).toFixed(
        2,
      )} °C`,
      icon: <FaExclamationTriangle />,
      color: "#f59e0b",
    },
    {
      title: "Prediction",
      value: prediction,
      icon: <MdOutlinePsychology />,
      color: "#8b5cf6",
    },
    {
      title: "Altitude",
      value: `${Number(telemetry["Altitude (km)"] ?? 0).toFixed(2)} km`,
      icon: <FaSatellite />,
      color: "#3b82f6",
    },
  ];

  return (
    <section className="kpi-grid">
      {cards.map((card) => (
        <div className="kpi-card" key={card.title}>
          <div
            className="kpi-icon"
            style={{
              background: `${card.color}20`,
              color: card.color,
            }}
          >
            {card.icon}
          </div>

          <div className="kpi-content">
            <span>{card.title}</span>
            <h2>{card.value}</h2>
          </div>
        </div>
      ))}
    </section>
  );
}

export default KPISection;
