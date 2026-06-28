import "./PredictionSummary.css";
import { FaCheckCircle } from "react-icons/fa";

function PredictionSummary() {
    return (
        <section className="prediction-summary">

            <div className="prediction-header">
                <h3>AI Prediction Summary</h3>
            </div>

            <div className="prediction-status">

                <FaCheckCircle className="status-icon" />

                <h2>Waiting for API</h2>

                <p>
                    XGBoost prediction will appear here after backend integration.
                </p>

            </div>

            <div className="prediction-footer">

                <div>
                    <span>Model</span>
                    <strong>XGBoost</strong>
                </div>

                <div>
                    <span>Confidence</span>
                    <strong>--%</strong>
                </div>

            </div>

        </section>
    );
}

export default PredictionSummary;