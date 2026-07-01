import "./SubsystemHealth.css";

function SubsystemHealth({ data }) {
  if (!data?.telemetry) return null;

  const t = data.telemetry;

  const clamp = (v) => Math.max(0, Math.min(100, Math.round(v)));

  const power = clamp(((t["BusVoltage (V)"] ?? 28) / 32) * 100);

  const battery = clamp(t["BatterySOC (%)"] ?? 0);

  const thermal = (() => {
    const temp = t["BatteryTemperature (°C)"] ?? 25;

    if (temp >= 15 && temp <= 40) return 100;
    if (temp >= 10 && temp <= 45) return 90;
    if (temp >= 5 && temp <= 50) return 75;
    return 50;
  })();

  const communication = (() => {
    const signal = t["SignalStrength (dBm)"] ?? -90;

    if (signal >= -80) return 100;
    if (signal >= -90) return 95;
    if (signal >= -100) return 85;
    if (signal >= -110) return 70;
    return 50;
  })();

  const adcs = (() => {
    const rpm = Math.abs(t["WheelRPM (RPM)"] ?? 0);

    if (rpm <= 3000) return 100;
    if (rpm <= 5000) return 90;
    if (rpm <= 7000) return 75;
    return 55;
  })();

  const obc = (() => {
    const cpu = t["CPUUsage (%)"] ?? 0;

    if (cpu <= 40) return 100;
    if (cpu <= 60) return 95;
    if (cpu <= 80) return 85;
    if (cpu <= 90) return 70;
    return 50;
  })();

  const systems = [
    { name: "Power", health: power },
    { name: "Battery", health: battery },
    { name: "Thermal", health: thermal },
    { name: "Communication", health: communication },
    { name: "ADCS", health: adcs },
    { name: "OBC", health: obc },
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
                background: `conic-gradient(#22c55e ${
                  system.health * 3.6
                }deg,#1f2937 0deg)`,
              }}
            >
              <div className="circle-inner">{system.health}%</div>
            </div>

            <span>{system.name}</span>
          </div>
        ))}
      </div>
    </section>
  );
}

export default SubsystemHealth;
