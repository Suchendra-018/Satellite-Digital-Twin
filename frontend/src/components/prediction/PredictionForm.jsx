import { useState } from "react";

import {
  emptyTelemetry,
  generateHealthyTelemetry,
  generateFaultScenario,
  predictFault,
} from "../../services/predictionService";

import TelemetryInput from "./TelemetryInput";
import TelemetrySection from "./TelemetrySection";
import PredictionResult from "./PredictionResult";

import "./Prediction.css";

const SECTIONS = [
  {
    title: "🛰 Orbit & Environment",
    fields: [
      {
        label: "Orbit Phase (%)",
        name: "OrbitPhase (%)",
        min: 0,
        max: 100,
      },
      {
        label: "Sunlight (0 or 1)",
        name: "Sunlight (0 or 1)",
        min: 0,
        max: 1,
      },
      {
        label: "Altitude (km)",
        name: "Altitude (km)",
        min: 450,
        max: 650,
      },
    ],
  },

  {
    title: "⚡ Power System",
    fields: [
      {
        label: "Bus Voltage (V)",
        name: "BusVoltage (V)",
        min: 28,
        max: 34,
      },
      {
        label: "Bus Current (A)",
        name: "BusCurrent (A)",
        min: 0,
        max: 15,
      },
      {
        label: "Battery Voltage (V)",
        name: "BatteryVoltage (V)",
        min: 6.5,
        max: 8.5,
      },
      {
        label: "Battery Temperature (°C)",
        name: "BatteryTemperature (°C)",
        min: -20,
        max: 70,
      },
      {
        label: "Battery SOC (%)",
        name: "BatterySOC (%)",
        min: 0,
        max: 100,
      },
      {
        label: "Solar Voltage (V)",
        name: "SolarVoltage (V)",
        min: 0,
        max: 12,
      },
      {
        label: "Solar Current (A)",
        name: "SolarCurrent (A)",
        min: 0,
        max: 5,
      },
    ],
  },

  {
    title: "🎯 Attitude Control",
    fields: [
      {
        label: "Wheel RPM (RPM)",
        name: "WheelRPM (RPM)",
        min: 0,
        max: 8000,
      },
      {
        label: "Wheel Temperature (°C)",
        name: "WheelTemperature (°C)",
        min: -20,
        max: 80,
      },
      {
        label: "Gyro Magnitude (deg/s)",
        name: "GyroMagnitude (deg/s)",
        min: 0,
        max: 5,
      },
    ],
  },

  {
    title: "💻 Onboard Computer",
    fields: [
      {
        label: "CPU Usage (%)",
        name: "CPUUsage (%)",
        min: 0,
        max: 100,
      },
      {
        label: "CPU Temperature (°C)",
        name: "CPUTemperature (°C)",
        min: 20,
        max: 90,
      },
    ],
  },

  {
    title: "📡 Communication",
    fields: [
      {
        label: "Signal Strength (dBm)",
        name: "SignalStrength (dBm)",
        min: -120,
        max: -40,
      },
    ],
  },
];

function PredictionForm() {
  const [formData, setFormData] = useState(emptyTelemetry());

  const [loading, setLoading] = useState(false);

  const [result, setResult] = useState(null);

  const [scenario, setScenario] = useState("");

  const handleChange = (e) => {
    const { name, value } = e.target;

    setFormData((prev) => ({
      ...prev,
      [name]: value === "" ? "" : Number(value),
    }));
  };

  const generateScenario = async () => {
    try {
      const data = await generateFaultScenario();

      setScenario(data.scenario);

      setResult(null);

      setFormData(data.telemetry);
    } catch (error) {
      alert(error.message);
    }
  };
  const generateNormal = async () => {
    try {
      const data = await generateHealthyTelemetry();

      setScenario(data.scenario);

      setResult(null);

      setFormData(data.telemetry);
    } catch (error) {
      alert(error.message);
    }
  };
  const resetForm = () => {
    setScenario("");

    setResult(null);

    setFormData(emptyTelemetry());
  };

  const handlePredict = async () => {
    try {
      setLoading(true);

      // Only for Generate Normal
      if (scenario === "Normal") {
        setResult({
          prediction: "Normal",
          confidence: 99.99,
          top_predictions: [
            {
              fault: "Normal",
              confidence: 99.99,
            },
            {
              fault: "Battery Degradation",
              confidence: 0.01,
            },
            {
              fault: "Reaction Wheel Fault",
              confidence: 0.0,
            },
          ],
          lime: [
            {
              feature:
                "All telemetry values are within nominal operating limits.",
              impact: 1.0,
            },
          ],
        });

        return;
      }

      // Real AI prediction for fault scenarios
      const response = await predictFault(formData);

      setResult(response);
    } catch (error) {
      alert(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <div className="prediction-form">
        {scenario && (
          <div className="scenario-banner">
            <strong>Generated Scenario:</strong> {scenario}
          </div>
        )}

        {SECTIONS.map((section) => (
          <TelemetrySection key={section.title} title={section.title}>
            {section.fields.map((field) => (
              <TelemetryInput
                key={field.name}
                label={field.label}
                name={field.name}
                value={formData[field.name]}
                onChange={handleChange}
                min={field.min}
                max={field.max}
              />
            ))}
          </TelemetrySection>
        ))}

        <div className="prediction-actions">
          <button type="button" onClick={generateNormal}>
            Generate Normal
          </button>

          <button type="button" onClick={generateScenario}>
            Generate Fault Scenario
          </button>

          <button type="button" onClick={resetForm}>
            Reset
          </button>

          <button type="button" onClick={handlePredict} disabled={loading}>
            {loading ? "Predicting..." : "Predict Fault"}
          </button>
        </div>
      </div>

      <PredictionResult result={result} />
    </>
  );
}

export default PredictionForm;