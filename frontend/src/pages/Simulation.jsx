import { useEffect, useState } from "react";
import { useLive } from "../context/LiveContext";

import { FaPlay, FaPause, FaRedo } from "react-icons/fa";

import { getDashboardData } from "../services/dashboardService";

import TelemetryCards from "../components/telemetry/TelemetryCards";
import LiveChart from "../components/telemetry/LiveChart";
import PredictionSummary from "../components/prediction/PredictionSummary";

function Simulation() {
  const [data, setData] = useState(null);
  const [running, setRunning] = useState(true);
  const { isLive } = useLive();
  useEffect(() => {
    let timer;

    const load = async () => {
      try {
        const response = await getDashboardData();
        setData(response);
      } catch (err) {
        console.error(err);
      }
    };

    load();

    if (running && isLive) {
      timer = setInterval(load, 1000);
    }

    return () => clearInterval(timer);
  }, [running, isLive]);

  if (!data) return <h2>Loading Simulation...</h2>;

  return (
    <>
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          marginBottom: 24,
        }}
      >
        <h2
          style={{
            color: "white",
          }}
        >
          Digital Twin Simulation
        </h2>

        <div
          style={{
            display: "flex",
            gap: 12,
          }}
        >
          <button onClick={() => setRunning(true)}>
            <FaPlay />
          </button>

          <button onClick={() => setRunning(false)}>
            <FaPause />
          </button>

          <button onClick={() => window.location.reload()}>
            <FaRedo />
          </button>
        </div>
      </div>

      <div className="dashboard-grid">
        <LiveChart data={data} />
        <PredictionSummary data={data} />
      </div>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "2fr 1fr",
          gap: 20,
          marginTop: 20,
        }}
      >
        <TelemetryCards data={data} />

        <div
          style={{
            background: "#111827",
            borderRadius: 18,
            padding: 20,
            color: "white",
            border: "1px solid rgba(255,255,255,.08)",
          }}
        >
          <h3 style={{ marginBottom: 18 }}>Simulation Status</h3>

          <p>
            <strong>Mode:</strong> {running ? "Running" : "Paused"}
          </p>

          <p>
            <strong>Mission:</strong> CubeSat-1
          </p>

          <p>
            <strong>Orbit:</strong> LEO
          </p>

          <p>
            <strong>Altitude:</strong>{" "}
            {data.telemetry["Altitude (km)"].toFixed(2)} km
          </p>

          <p>
            <strong>Health:</strong> {data.health_score}%
          </p>

          <p>
            <strong>Prediction:</strong> {data.prediction.fault_name}
          </p>

          <p>
            <strong>Confidence:</strong> {data.confidence}%
          </p>
        </div>
      </div>
    </>
  );
}

export default Simulation;
