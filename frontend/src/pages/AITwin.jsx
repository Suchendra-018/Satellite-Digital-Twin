import { useEffect, useState } from "react";
import { useLive } from "../context/LiveContext";

import { getDashboardData } from "../services/dashboardService";

import PredictionSummary from "../components/prediction/PredictionSummary";
import LiveChart from "../components/telemetry/LiveChart";
import TelemetryCards from "../components/telemetry/TelemetryCards";
import SubsystemHealth from "../components/dashboard/SubsystemHealth";

function AITwin() {
  const [data, setData] = useState(null);
  const { isLive } = useLive();
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await getDashboardData();
        setData(response);
      } catch (e) {
        console.error(e);
      }
    };

    if (!isLive) return;

    fetchData();

    const timer = setInterval(fetchData, 1000);

    return () => clearInterval(timer);
  }, [isLive]);

  if (!data) return <h2>Loading AI Twin...</h2>;

  return (
    <>
      <PredictionSummary data={data} />

      <div className="dashboard-grid">
        <LiveChart data={data} />
        <SubsystemHealth data={data} />
      </div>

      <TelemetryCards data={data} />
    </>
  );
}

export default AITwin;
