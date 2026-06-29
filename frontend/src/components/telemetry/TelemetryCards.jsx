import "./TelemetryCards.css";

function TelemetryCards({ data }) {
    if (!data || !data.telemetry) return null;

    const telemetry = data.telemetry;

    const cards = [
        {
            title: "Bus Voltage",
            value: `${telemetry["BusVoltage (V)"].toFixed(2)} V`
        },
        {
            title: "Battery Temp",
            value: `${telemetry["BatteryTemperature (°C)"].toFixed(1)} °C`
        },
        {
            title: "Battery SOC",
            value: `${telemetry["BatterySOC (%)"].toFixed(1)} %`
        },
        {
            title: "CPU Temp",
            value: `${telemetry["CPUTemperature (°C)"].toFixed(1)} °C`
        },
        {
            title: "Signal Strength",
            value: `${telemetry["SignalStrength (dBm)"]} dBm`,
        },
        {
            title: "Wheel RPM",
            value: `${telemetry["WheelRPM (RPM)"]} RPM`,
        },
    ];

    return (
        <section className="telemetry-cards">
            {cards.map((item) => (
                <div className="telemetry-card" key={item.title}>
                    <span>{item.title}</span>
                    <h3>{item.value}</h3>
                </div>
            ))}
        </section>
    );
}

export default TelemetryCards;