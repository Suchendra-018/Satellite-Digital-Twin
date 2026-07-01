import "./Navbar.css";

import { NavLink } from "react-router-dom";
import { FaCircle } from "react-icons/fa";
import { useEffect, useState } from "react";

function Navbar() {
  const [utcTime, setUtcTime] = useState("");

  useEffect(() => {
    const updateClock = () => {
      setUtcTime(
        new Date().toLocaleTimeString("en-GB", {
          timeZone: "UTC",
          hour12: false,
        }) + " UTC",
      );
    };

    updateClock();

    const timer = setInterval(updateClock, 1000);

    return () => clearInterval(timer);
  }, []);

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

        <strong>{utcTime}</strong>
      </div>
    </header>
  );
}

export default Navbar;
