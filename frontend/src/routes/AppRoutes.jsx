import { BrowserRouter, Routes, Route } from "react-router-dom";

import MainLayout from "../layouts/MainLayout";

import Dashboard from "../pages/Dashboard";
import Analytics from "../pages/Analytics";
import Simulation from "../pages/Simulation";
import AITwin from "../pages/AITwin";
import Security from "../pages/Security";
import NotFound from "../pages/NotFound";

function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<MainLayout />}>
          <Route path="/" element={<Dashboard />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/analytics" element={<Analytics />} />
          <Route path="/simulation" element={<Simulation />} />
          <Route path="/ai-twin" element={<AITwin />} />
          <Route path="/security" element={<Security />} />
        </Route>

        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}

export default AppRoutes;
