import "./LiveChart.css";

import { useEffect, useState } from "react";

import {
  ResponsiveContainer,
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
} from "recharts";

function LiveChart({ data }) {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    if (!data?.telemetry) return;

    const t = data.telemetry;

    const point = {
      sample: data.sample ?? history.length + 1,
      voltage: Number(t["BusVoltage (V)"] ?? 0),
      battery: Number(t["BatterySOC (%)"] ?? 0),
      temperature: Number(t["BatteryTemperature (°C)"] ?? 0),
      cpu: Number(t["CPUUsage (%)"] ?? 0),
      signal: Number(t["SignalStrength (dBm)"] ?? 0),
    };

    setHistory((prev) => {
      const updated = [...prev, point];

      if (updated.length > 30) {
        updated.shift();
      }

      return updated;
    });
  }, [data]);

  return (
    <section className="live-chart">
      <div className="live-chart-header">
        <div>
          <h3>Live Telemetry</h3>
          <p>Real-time CubeSat Telemetry Stream</p>
        </div>

        <span className="live-status">● LIVE</span>
      </div>

      <ResponsiveContainer width="100%" height={340}>
        <LineChart data={history}>
          <CartesianGrid stroke="#1f2937" strokeDasharray="4 4" />

          <XAxis dataKey="sample" stroke="#94a3b8" />

          <YAxis stroke="#94a3b8" />

          <Tooltip />

          <Legend />

          <Line
            type="monotone"
            dataKey="voltage"
            name="Bus Voltage"
            stroke="#3b82f6"
            strokeWidth={2}
            dot={false}
          />

          <Line
            type="monotone"
            dataKey="battery"
            name="Battery SOC"
            stroke="#22c55e"
            strokeWidth={2}
            dot={false}
          />

          <Line
            type="monotone"
            dataKey="temperature"
            name="Temperature"
            stroke="#f59e0b"
            strokeWidth={2}
            dot={false}
          />

          <Line
            type="monotone"
            dataKey="cpu"
            name="CPU Usage"
            stroke="#a855f7"
            strokeWidth={2}
            dot={false}
          />

          <Line
            type="monotone"
            dataKey="signal"
            name="Signal"
            stroke="#ef4444"
            strokeWidth={2}
            dot={false}
          />
        </LineChart>
      </ResponsiveContainer>
    </section>
  );
}

export default LiveChart;
