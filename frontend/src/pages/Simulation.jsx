import { useEffect, useState } from "react";

import { FaPlay, FaPause, FaRedo } from "react-icons/fa";

import { getDashboardData } from "../services/dashboardService";

import TelemetryCards from "../components/telemetry/TelemetryCards";
import LiveChart from "../components/telemetry/LiveChart";
import PredictionSummary from "../components/prediction/PredictionSummary";

function Simulation() {
  const [data, setData] = useState(null);
  const [running, setRunning] = useState(true);

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

    if (running) {
      timer = setInterval(load, 1000);
    }

    return () => clearInterval(timer);
  }, [running]);

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

      <TelemetryCards data={data} />
    </>
  );
}

export default Simulation;
