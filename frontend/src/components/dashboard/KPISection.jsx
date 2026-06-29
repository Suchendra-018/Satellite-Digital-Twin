import "./KPISection.css";

import {
    FaHeartbeat,
    FaExclamationTriangle,
    FaSatellite,
} from "react-icons/fa";

import { MdOutlinePsychology } from "react-icons/md";

function KPISection({ data }) {

    if (!data) return null;

    const telemetry = data.telemetry;

    const cards = [

        {
            title: "Battery Voltage",
            value: `${telemetry["BatteryVoltage (V)"]} V`,
            icon: <FaHeartbeat />,
            color: "#22c55e",
        },

        {
            title: "Battery Temperature",
            value: `${telemetry["BatteryTemperature (°C)"]} °C`,
            icon: <FaExclamationTriangle />,
            color: "#f59e0b",
        },

        {
            title: "Prediction",
            value: data.prediction === 0 ? "Normal" : "Fault",
            icon: <MdOutlinePsychology />,
            color: "#8b5cf6",
        },

        {
            title: "Altitude",
            value: `${telemetry["Altitude (km)"]} km`,
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