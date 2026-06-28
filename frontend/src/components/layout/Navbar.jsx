import "./Navbar.css";

import { NavLink } from "react-router-dom";
import { FaCircle } from "react-icons/fa";

function Navbar() {
    return (
        <header className="navbar">

            <div className="navbar-left">

                <div className="live-badge">
                    <FaCircle />
                    LIVE
                </div>

                <nav className="top-menu">

                    <NavLink to="/dashboard">Dashboard</NavLink>

                    <NavLink to="/ai-twin">AI Twin</NavLink>

                    <NavLink to="/analytics">Analytics</NavLink>

                    <NavLink to="/simulation">Simulation</NavLink>

                    <NavLink to="/security">Security</NavLink>

                </nav>

            </div>

            <div className="mission-status">

                <span>Mission Time</span>

                <strong>02:17:43 UTC</strong>

            </div>

        </header>
    );
}

export default Navbar;