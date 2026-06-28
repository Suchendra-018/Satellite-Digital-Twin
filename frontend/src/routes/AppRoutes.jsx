import { Routes, Route, Navigate } from "react-router-dom";

import MainLayout from "../layouts/MainLayout";

import Dashboard from "../pages/Dashboard";
import AITwin from "../pages/AITwin";
import Analytics from "../pages/Analytics";
import Simulation from "../pages/Simulation";
import Security from "../pages/Security";
import NotFound from "../pages/NotFound";

function AppRoutes() {
    return (
        <Routes>
            <Route element={<MainLayout />}>
                <Route path="/" element={<Navigate to="/dashboard" replace />} />

                <Route path="/dashboard" element={<Dashboard />} />
                <Route path="/ai-twin" element={<AITwin />} />
                <Route path="/analytics" element={<Analytics />} />
                <Route path="/simulation" element={<Simulation />} />
                <Route path="/security" element={<Security />} />
            </Route>

            <Route path="*" element={<NotFound />} />
        </Routes>
    );
}

export default AppRoutes;