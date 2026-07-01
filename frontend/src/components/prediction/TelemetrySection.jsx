function TelemetrySection({ title, children }) {
  return (
    <div className="telemetry-section">
      <h3>{title}</h3>

      <div className="telemetry-grid">{children}</div>
    </div>
  );
}

export default TelemetrySection;
