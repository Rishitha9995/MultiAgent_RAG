import React, { useState } from "react";
import "./App.css";
import Header from "./components/Header";
import Sidebar from "./components/Sidebar";
import Chat from "./components/Chat";

function App() {
  const [active, setActive] = useState("chat");
  const [, setMetrics] = useState(null); // ✅ fixed

  const handleMenuClick = (item) => {
    setActive(item);
  };

  return (
    <div className="app">
      <Header />

      <div className="main">
        <Sidebar active={active} handleMenuClick={handleMenuClick} />

        <div className="content">
          {active === "chat" && <Chat setMetrics={setMetrics} />}
        </div>
      </div>
    </div>
  );
}

export default App;