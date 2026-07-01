import "./AlertList.css";
import { FaCheckCircle, FaExclamationTriangle } from "react-icons/fa";

function AlertList({ data }) {
  if (!data?.telemetry) return null;

  const t = data.telemetry;

  const alerts = [];

  if ((t["BatteryTemperature (°C)"] ?? 0) > 45) {
    alerts.push({
      type: "warning",
      title: "Battery Temperature High",
      time: "Now",
    });
  }

  if ((t["CPUUsage (%)"] ?? 0) > 90) {
    alerts.push({
      type: "warning",
      title: "High CPU Usage",
      time: "Now",
    });
  }

  if ((t["SignalStrength (dBm)"] ?? 0) < -105) {
    alerts.push({
      type: "warning",
      title: "Weak Communication Signal",
      time: "Now",
    });
  }

  if ((t["WheelRPM (RPM)"] ?? 0) > 7000) {
    alerts.push({
      type: "warning",
      title: "Reaction Wheel Overspeed",
      time: "Now",
    });
  }

  if (alerts.length === 0) {
    alerts.push({
      type: "success",
      title: "Satellite Operating Normally",
      time: "Live",
    });
  }

  return (
    <section className="alert-list">
      <div className="alert-header">
        <h3>Recent Alerts</h3>
        <span>{alerts.length} Events</span>
      </div>

      {alerts.map((alert, index) => (
        <div key={index} className={`alert ${alert.type}`}>
          {alert.type === "success" ? (
            <FaCheckCircle />
          ) : (
            <FaExclamationTriangle />
          )}

          <div>
            <h4>{alert.title}</h4>
            <p>{alert.time}</p>
          </div>
        </div>
      ))}
    </section>
  );
}

export default AlertList;
