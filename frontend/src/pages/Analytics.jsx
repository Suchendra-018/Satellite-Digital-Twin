import { useEffect, useState } from "react";

import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

import { getDashboardData } from "../services/dashboardService";

function Analytics() {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    const load = async () => {
      try {
        const data = await getDashboardData();

        setHistory((prev) => {
          const next = [
            ...prev,
            {
              sample: data.sample,
              voltage: data.telemetry["BusVoltage (V)"],
              battery: data.telemetry["BatterySOC (%)"],
              cpu: data.telemetry["CPUUsage (%)"],
              temp: data.telemetry["BatteryTemperature (°C)"],
            },
          ];

          return next.slice(-25);
        });
      } catch (err) {
        console.error(err);
      }
    };

    load();

    const timer = setInterval(load, 1000);

    return () => clearInterval(timer);
  }, []);

  return (
    <div
      style={{
        background: "#111827",
        padding: 25,
        borderRadius: 18,
        border: "1px solid rgba(255,255,255,.08)",
      }}
    >
      <h2
        style={{
          color: "white",
          marginBottom: 25,
        }}
      >
        Telemetry Analytics
      </h2>

      <ResponsiveContainer width="100%" height={450}>
        <LineChart data={history}>
          <CartesianGrid strokeDasharray="3 3" />

          <XAxis dataKey="sample" />

          <YAxis />

          <Tooltip />

          <Line dataKey="voltage" stroke="#3b82f6" dot={false} />

          <Line dataKey="battery" stroke="#22c55e" dot={false} />

          <Line dataKey="cpu" stroke="#f59e0b" dot={false} />

          <Line dataKey="temp" stroke="#ef4444" dot={false} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

export default Analytics;
