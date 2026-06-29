import { useEffect, useState } from "react";

import Hero from "../components/dashboard/Hero";
import KPISection from "../components/dashboard/KPISection";
import SubsystemHealth from "../components/dashboard/SubsystemHealth";

import LiveChart from "../components/telemetry/LiveChart";
import TelemetryCards from "../components/telemetry/TelemetryCards";

import AlertList from "../components/alerts/AlertList";
import PredictionSummary from "../components/prediction/PredictionSummary";

import { getDashboardData } from "../services/dashboardService";

import "./Dashboard.css";

function Dashboard() {

    const [dashboardData, setDashboardData] = useState(null);

    const [loading, setLoading] = useState(true);

    useEffect(() => {

        async function fetchDashboard() {

            try {

                const data = await getDashboardData();
                console.log("Dashboard API Response:", data);
                setDashboardData(data);
                

            } catch (error) {

                console.error(error);

            } finally {

                setLoading(false);

            }

        }

        fetchDashboard();

    }, []);

    if (loading) {

        return <h2>Loading Dashboard...</h2>;

    }

    return (
        <>

            <Hero />

            <KPISection data={dashboardData} />

            <div className="dashboard-grid">

                <LiveChart data={dashboardData} />

                <AlertList data={dashboardData} />

            </div>

            <div className="dashboard-grid">

                <SubsystemHealth data={dashboardData} />

                <PredictionSummary data={dashboardData} />

            </div>

            <TelemetryCards data={dashboardData} />

        </>
    );

}

export default Dashboard;