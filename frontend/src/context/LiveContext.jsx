import { createContext, useContext, useState } from "react";

const LiveContext = createContext();

export function LiveProvider({ children }) {
  const [isLive, setIsLive] = useState(true);

  const toggleLive = () => {
    setIsLive((prev) => !prev);
  };

  return (
    <LiveContext.Provider
      value={{
        isLive,
        toggleLive,
      }}
    >
      {children}
    </LiveContext.Provider>
  );
}

export function useLive() {
  return useContext(LiveContext);
}
