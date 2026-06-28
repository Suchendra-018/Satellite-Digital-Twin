import "./LiveChart.css";

function LiveChart() {
    return (
        <section className="live-chart">

            <div className="live-chart-header">
                <div>
                    <h3>Live Telemetry</h3>
                    <p>Real-time CubeSat sensor monitoring</p>
                </div>

                <span className="live-status">
                    ● LIVE
                </span>
            </div>

            <div className="chart-placeholder">
                Telemetry Graph (Coming Next)
            </div>

        </section>
    );
}

export default LiveChart;