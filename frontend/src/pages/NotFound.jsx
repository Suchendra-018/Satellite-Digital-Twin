import { Link } from "react-router-dom";

function NotFound() {
  return (
    <div
      style={{
        minHeight: "80vh",
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        color: "white",
        textAlign: "center",
      }}
    >
      <h1
        style={{
          fontSize: "90px",
          margin: 0,
          color: "#3b82f6",
        }}
      >
        404
      </h1>

      <h2>Page Not Found</h2>

      <p
        style={{
          color: "#94a3b8",
          marginBottom: 30,
        }}
      >
        The page you are looking for does not exist.
      </p>

      <Link
        to="/dashboard"
        style={{
          background: "#2563eb",
          color: "white",
          padding: "14px 24px",
          borderRadius: "12px",
          textDecoration: "none",
          fontWeight: 600,
        }}
      >
        Back to Dashboard
      </Link>
    </div>
  );
}

export default NotFound;
