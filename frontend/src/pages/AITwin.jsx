import { useEffect, useState } from "react";

import { getDashboardData } from "../services/dashboardService";

import PredictionSummary from "../components/prediction/PredictionSummary";
import LiveChart from "../components/telemetry/LiveChart";
import TelemetryCards from "../components/telemetry/TelemetryCards";
import SubsystemHealth from "../components/dashboard/SubsystemHealth";

function AITwin() {
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await getDashboardData();
        setData(response);
      } catch (e) {
        console.error(e);
      }
    };

    fetchData();

    const timer = setInterval(fetchData, 1000);

    return () => clearInterval(timer);
  }, []);

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
