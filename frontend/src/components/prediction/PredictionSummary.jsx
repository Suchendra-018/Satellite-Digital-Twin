import "./PredictionSummary.css";
import {
  FaCheckCircle,
  FaExclamationTriangle,
  FaTimesCircle,
} from "react-icons/fa";

function PredictionSummary({ data }) {
  if (!data) return null;

  const prediction = data.prediction ?? {};

  const fault = prediction.fault_name ?? "Unknown";
  const confidence = prediction.confidence ?? "--";
  const health = data.health_score ?? "--";
  const alert = data.alert_level ?? "--";

  let Icon = FaCheckCircle;
  let statusClass = "normal";

  if (alert === "WARNING") {
    Icon = FaExclamationTriangle;
    statusClass = "warning";
  }

  if (alert === "CRITICAL") {
    Icon = FaTimesCircle;
    statusClass = "critical";
  }

  return (
    <section className="prediction-summary">
      <div className="prediction-header">
        <h3>AI Prediction Summary</h3>
      </div>

      <div className={`prediction-status ${statusClass}`}>
        <Icon className="status-icon" />

        <h2>{fault}</h2>

        <p>Live fault prediction from the XGBoost Digital Twin.</p>
      </div>

      <div className="prediction-footer">
        <div>
          <span>Model</span>
          <strong>XGBoost</strong>
        </div>

        <div>
          <span>Confidence</span>
          <strong>{confidence}%</strong>
        </div>

        <div>
          <span>Health</span>
          <strong>{health}%</strong>
        </div>

        <div>
          <span>Alert</span>
          <strong>{alert}</strong>
        </div>
      </div>
    </section>
  );
}

export default PredictionSummary;
