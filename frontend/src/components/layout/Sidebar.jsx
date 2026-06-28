import {
    MdDashboard,
    MdOutlineAnalytics,
    MdSecurity,
    MdSettings,
} from "react-icons/md";

import {
    FaSatelliteDish,
    FaRobot,
} from "react-icons/fa";

import { NavLink } from "react-router-dom";

import "./Sidebar.css";

const menu = [
    {
        name: "Dashboard",
        icon: <MdDashboard />,
        path: "/dashboard",
    },
    {
        name: "Telemetry",
        icon: <FaSatelliteDish />,
        path: "/simulation",
    },
    {
        name: "AI Twin",
        icon: <FaRobot />,
        path: "/ai-twin",
    },
    {
        name: "Analytics",
        icon: <MdOutlineAnalytics />,
        path: "/analytics",
    },
    {
        name: "Security",
        icon: <MdSecurity />,
        path: "/security",
    },
];

function Sidebar() {
    return (
        <aside className="sidebar">
            <div className="logo">
                🛰
                <div>
                    <h2>Satellite</h2>
                    <span>Digital Twin</span>
                </div>
            </div>

            <nav className="menu">
                {menu.map((item) => (
                    <NavLink
                        key={item.name}
                        to={item.path}
                        className={({ isActive }) =>
                            `link ${isActive ? "active" : ""}`
                        }
                    >
                        {item.icon}
                        <span>{item.name}</span>
                    </NavLink>
                ))}
            </nav>

            <div className="bottom">
                <button className="settings">
                    <MdSettings />
                    Settings
                </button>
            </div>
        </aside>
    );
}

export default Sidebar;