import { useEffect, useState } from "react";

import { FaShieldAlt, FaLock, FaWifi, FaServer } from "react-icons/fa";

function Security() {
  const [time, setTime] = useState("");

  useEffect(() => {
    const update = () => {
      setTime(new Date().toLocaleTimeString());
    };

    update();

    const timer = setInterval(update, 1000);

    return () => clearInterval(timer);
  }, []);

  const cards = [
    {
      title: "Encryption",
      value: "AES-256",
      icon: <FaLock />,
      color: "#22c55e",
    },
    {
      title: "Communication",
      value: "SECURE",
      icon: <FaWifi />,
      color: "#3b82f6",
    },
    {
      title: "Firewall",
      value: "ACTIVE",
      icon: <FaShieldAlt />,
      color: "#f59e0b",
    },
    {
      title: "Ground Server",
      value: "ONLINE",
      icon: <FaServer />,
      color: "#8b5cf6",
    },
  ];

  return (
    <>
      <h1
        style={{
          color: "white",
          marginBottom: 10,
        }}
      >
        Security Center
      </h1>

      <p
        style={{
          color: "#94a3b8",
          marginBottom: 30,
        }}
      >
        Last Security Check : {time}
      </p>

      <div className="kpi-grid">
        {cards.map((card) => (
          <div className="kpi-card" key={card.title}>
            <div
              className="kpi-icon"
              style={{
                background: `${card.color}20`,
                color: card.color,
              }}
            >
              {card.icon}
            </div>

            <div className="kpi-content">
              <span>{card.title}</span>
              <h2>{card.value}</h2>
            </div>
          </div>
        ))}
      </div>

      <div
        style={{
          marginTop: 30,
          background: "#111827",
          borderRadius: 18,
          border: "1px solid rgba(255,255,255,.08)",
          padding: 25,
        }}
      >
        <h2
          style={{
            color: "white",
            marginBottom: 20,
          }}
        >
          Security Status
        </h2>

        <ul
          style={{
            color: "#cbd5e1",
            lineHeight: 2,
          }}
        >
          <li>✓ Secure Telemetry Channel</li>
          <li>✓ AI Model Integrity Verified</li>
          <li>✓ Ground Station Connected</li>
          <li>✓ Authentication Active</li>
          <li>✓ No Intrusion Detected</li>
        </ul>
      </div>
    </>
  );
}

export default Security;
