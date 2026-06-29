import "./SubsystemHealth.css";

function SubsystemHealth({ data }) {
    if (!data || !data.telemetry) return null;

    const t = data.telemetry;

    const systems = [
        {
            name: "Power",
            health: t["BusVoltage (V)"] >= 30 ? 98 : 70,
        },
        {
            name: "Battery",
            health: t["BatterySOC (%)"] >= 50 ? 95 : 60,
        },
        {
            name: "Thermal",
            health:
                t["BatteryTemperature (°C)"] >= 15 &&
                    t["BatteryTemperature (°C)"] <= 45
                    ? 97
                    : 65,
        },
        {
            name: "Communication",
            health: t["SignalStrength (dBm)"] >= -100 ? 96 : 75,
        },
        {
            name: "ADCS",
            health: Math.abs(t["WheelRPM (RPM)"]) <= 5000 ? 94 : 70,
        },
        {
            name: "OBC",
            health: t["CPUUsage (%)"] <= 80 ? 95 : 65,
        },
    ];

    return (
        <section className="subsystem-health">
            <div className="subsystem-header">
                <h3>Subsystem Health</h3>
            </div>

            <div className="subsystem-grid">
                {systems.map((system) => (
                    <div className="system-card" key={system.name}>
                        <div
                            className="circle"
                            style={{
                                background: `conic-gradient(#22c55e ${system.health * 3.6}deg,#1f2937 0deg)`,
                            }}
                        >
                            <div className="circle-inner">
                                {system.health}%
                            </div>
                        </div>

                        <span>{system.name}</span>
                    </div>
                ))}
            </div>
        </section>
    );
}

export default SubsystemHealth;