import "./Hero.css";

function Hero() {
  const date = new Date().toLocaleString();

  return (
    <section className="hero">
      <div className="hero-content">
        <span className="hero-badge">● SATELLITE DIGITAL TWIN</span>

        <h1>
          AI Powered
          <br />
          <span>CubeSat Mission Control</span>
        </h1>

        <p>
          Real-time telemetry • Fault Prediction • Digital Twin • XGBoost • LSTM
          • Explainable AI
        </p>

        <div className="hero-info">
          <div className="hero-item">
            <span>Status</span>
            <strong>ONLINE</strong>
          </div>

          <div className="hero-item">
            <span>Mission</span>
            <strong>CubeSat-1</strong>
          </div>

          <div className="hero-item">
            <span>Mode</span>
            <strong>NOMINAL</strong>
          </div>

          <div className="hero-item">
            <span>Time</span>
            <strong>{date}</strong>
          </div>
        </div>
      </div>
    </section>
  );
}

export default Hero;
