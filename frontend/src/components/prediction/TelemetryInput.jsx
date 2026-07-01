function TelemetryInput({
  label,
  name,
  value,
  onChange,
  placeholder,
  min,
  max,
}) {
  const number = value === "" ? "" : Number(value);

  const outOfRange =
    value !== "" &&
    ((min !== undefined && number < min) ||
      (max !== undefined && number > max));

  return (
    <div className="telemetry-input">
      <label>{label}</label>

      <input
        type="number"
        step="any"
        name={name}
        value={value}
        placeholder={placeholder}
        onChange={onChange}
      />

      <small>
        Expected Range: {min} - {max}
      </small>

      {outOfRange && (
        <p className="warning">⚠ Outside expected operating range.</p>
      )}
    </div>
  );
}

export default TelemetryInput;
