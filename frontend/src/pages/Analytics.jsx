import { useEffect, useMemo, useState } from "react";

import {
  LineChart,
  Line,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

import { useLive } from "../context/LiveContext";
import { getDashboardData } from "../services/dashboardService";

import "./Dashboard.css";

function Analytics() {
  const [history, setHistory] = useState([]);

  const { isLive } = useLive();

  useEffect(() => {
    const load = async () => {
      try {
        const data = await getDashboardData();

        setHistory((prev) => {
          const next = [
            ...prev,
            {
              sample: data.sample,
              prediction: data.prediction.fault_name,
              confidence: data.confidence,
              health: data.health_score,
              voltage: data.telemetry["BusVoltage (V)"],
              battery: data.telemetry["BatterySOC (%)"],
              cpu: data.telemetry["CPUUsage (%)"],
              temperature: data.telemetry["BatteryTemperature (°C)"],
            },
          ];

          return next.slice(-30);
        });
      } catch (err) {
        console.error(err);
      }
    };

    if (!isLive) return;

    load();

    const timer = setInterval(load, 1000);

    return () => clearInterval(timer);
  }, [isLive]);

  const latest = history[history.length - 1];

  const faultDistribution = useMemo(() => {
    const map = {};

    history.forEach((item) => {
      map[item.prediction] = (map[item.prediction] || 0) + 1;
    });

    return Object.entries(map).map(([fault, count]) => ({
      fault,
      count,
    }));
  }, [history]);

  if (!latest) {
    return <h2>Loading Analytics...</h2>;
  }

  return (
    <div>
      <div className="dashboard-grid" style={{ marginBottom: 25 }}>
        <div className="kpi-card">
          <h4>Prediction</h4>
          <h2>{latest.prediction}</h2>
        </div>

        <div className="kpi-card">
          <h4>Confidence</h4>
          <h2>{latest.confidence}%</h2>
        </div>

        <div className="kpi-card">
          <h4>Health Score</h4>
          <h2>{latest.health}</h2>
        </div>

        <div className="kpi-card">
          <h4>Samples</h4>
          <h2>{history.length}</h2>
        </div>
      </div>

      <div
        style={{
          background: "#111827",
          padding: 20,
          borderRadius: 18,
          marginBottom: 25,
        }}
      >
        <h2 style={{ color: "white" }}>Live Telemetry</h2>

        <ResponsiveContainer width="100%" height={350}>
          <LineChart data={history}>
            <CartesianGrid strokeDasharray="3 3" />

            <XAxis dataKey="sample" />

            <YAxis />

            <Tooltip />

            <Line dataKey="voltage" stroke="#3b82f6" dot={false} />

            <Line dataKey="battery" stroke="#22c55e" dot={false} />

            <Line dataKey="cpu" stroke="#f59e0b" dot={false} />

            <Line dataKey="temperature" stroke="#ef4444" dot={false} />
          </LineChart>
        </ResponsiveContainer>
      </div>
      <div className="dashboard-grid" style={{ marginBottom: 25 }}>
        <div
          style={{
            background: "#111827",
            padding: 20,
            borderRadius: 18,
          }}
        >
          <h2 style={{ color: "white" }}>Prediction Confidence</h2>

          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={history}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="sample" />
              <YAxis domain={[0, 100]} />
              <Tooltip />

              <Line dataKey="confidence" stroke="#22c55e" dot={false} />
            </LineChart>
          </ResponsiveContainer>
        </div>

        <div
          style={{
            background: "#111827",
            padding: 20,
            borderRadius: 18,
          }}
        >
          <h2 style={{ color: "white" }}>Health Score Trend</h2>

          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={history}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="sample" />
              <YAxis domain={[0, 100]} />
              <Tooltip />

              <Line dataKey="health" stroke="#06b6d4" dot={false} />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>

      <div
        style={{
          background: "#111827",
          padding: 20,
          borderRadius: 18,
          marginBottom: 25,
        }}
      >
        <h2 style={{ color: "white" }}>Fault Distribution</h2>

        <ResponsiveContainer width="100%" height={320}>
          <BarChart data={faultDistribution}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="fault" />
            <YAxis />
            <Tooltip />

            <Bar dataKey="count" fill="#3b82f6" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      <div
        style={{
          background: "#111827",
          padding: 20,
          borderRadius: 18,
        }}
      >
        <h2
          style={{
            color: "white",
            marginBottom: 20,
          }}
        >
          Recent Prediction History
        </h2>

        <table
          style={{
            width: "100%",
            borderCollapse: "collapse",
            color: "white",
          }}
        >
          <thead>
            <tr>
              <th>Sample</th>
              <th>Prediction</th>
              <th>Confidence</th>
              <th>Health</th>
            </tr>
          </thead>

          <tbody>
            {[...history]
              .reverse()
              .slice(0, 10)
              .map((item) => (
                <tr
                  key={item.sample}
                  style={{
                    textAlign: "center",
                    height: 40,
                  }}
                >
                  <td>{item.sample}</td>

                  <td>{item.prediction}</td>

                  <td>{item.confidence}%</td>

                  <td>{item.health}</td>
                </tr>
              ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Analytics;