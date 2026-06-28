import { Outlet } from "react-router-dom";

import Sidebar from "../components/layout/Sidebar";
import Navbar from "../components/layout/Navbar";
import Footer from "../components/layout/Footer";
import "./MainLayout.css";
function MainLayout() {
    return (
        <>
            <Sidebar />

            <main
                style={{
                    marginLeft: "260px",
                    minHeight: "100vh",
                    background: "#050816",
                }}
            >
                <Navbar />

                <div className="page-content">
                    <>
                        <Outlet />
                        <Footer />
                    </>
                </div>
            </main>
        </>
    );
}

export default MainLayout;