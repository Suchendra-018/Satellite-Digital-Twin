import "./TelemetryCards.css";

const telemetry = [
    { title: "Bus Voltage", value: "-- V" },
    { title: "Battery Temp", value: "-- °C" },
    { title: "Battery SOC", value: "-- %" },
    { title: "CPU Temp", value: "-- °C" },
    { title: "Signal Strength", value: "-- dBm" },
    { title: "Wheel RPM", value: "-- RPM" },
];

function TelemetryCards() {
    return (
        <section className="telemetry-cards">

            {telemetry.map((item) => (
                <div className="telemetry-card" key={item.title}>
                    <span>{item.title}</span>
                    <h3>{item.value}</h3>
                </div>
            ))}

        </section>
    );
}

export default TelemetryCards;