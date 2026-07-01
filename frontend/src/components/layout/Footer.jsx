import "./Footer.css";

function Footer() {
  return (
    <footer className="footer">
      <div className="footer-left">
        <h4>Satellite Digital Twin</h4>
        <p>AI Powered CubeSat Monitoring & Fault Prediction</p>
      </div>

      <div className="footer-center">
        <span>Samsung Innovation Campus 2026</span>
      </div>

      <div className="footer-right">
        <span>Version 1.0.0</span>
        <span>System Status : ONLINE</span>
      </div>
    </footer>
  );
}

export default Footer;
