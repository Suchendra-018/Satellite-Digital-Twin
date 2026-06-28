import "./Hero.css";

function Hero() {
    return (
        <section className="hero">

            <div className="hero-content">

                <span className="hero-badge">
                    ● MISSION CONTROL
                </span>

                <h1>
                    Your Mission,
                    <br />
                    Decoded in <span>Real-Time</span>
                </h1>

                <p>
                    Advanced monitoring, predictive AI, anomaly detection and Digital
                    Twin technology for CubeSat health monitoring.
                </p>

                <button className="hero-btn">
                    Launch Mission Dashboard
                </button>

            </div>

        </section>
    );
}

export default Hero;