import "./AlertList.css";
import { FaExclamationTriangle, FaCheckCircle } from "react-icons/fa";

function AlertList() {
    return (
        <section className="alert-list">

            <div className="alert-header">
                <h3>Recent Alerts</h3>
                <span>3 Events</span>
            </div>

            <div className="alert warning">
                <FaExclamationTriangle />
                <div>
                    <h4>Battery Temperature High</h4>
                    <p>2 minutes ago</p>
                </div>
            </div>

            <div className="alert success">
                <FaCheckCircle />
                <div>
                    <h4>Communication Stable</h4>
                    <p>5 minutes ago</p>
                </div>
            </div>

            <div className="alert warning">
                <FaExclamationTriangle />
                <div>
                    <h4>Wheel RPM Fluctuation</h4>
                    <p>12 minutes ago</p>
                </div>
            </div>

        </section>
    );
}

export default AlertList;