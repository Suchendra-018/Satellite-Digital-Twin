import { Outlet } from "react-router-dom";

import Sidebar from "../components/layout/Sidebar";
import Navbar from "../components/layout/Navbar";
import Footer from "../components/layout/Footer";

import "./MainLayout.css";

function MainLayout() {
  return (
    <div className="layout">
      <Sidebar />

      <main className="main-content">
        <Navbar />

        <div className="page-content">
          <Outlet />
        </div>

        <Footer />
      </main>
    </div>
  );
}

export default MainLayout;
