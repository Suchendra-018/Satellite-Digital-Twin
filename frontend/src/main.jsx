import React from "react";
import ReactDOM from "react-dom/client";

import App from "./App.jsx";

import { LiveProvider } from "./context/LiveContext";

import "./styles/globals.css";
import "./styles/animations.css";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <LiveProvider>
      <App />
    </LiveProvider>
  </React.StrictMode>,
);
