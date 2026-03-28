import React from "react";

function Sidebar({ active, handleMenuClick }) {
  return (
    <div className="sidebar">
      <h3>Dashboard</h3>

      {["chat"].map(item => (
        <div
          key={item}
          onClick={() => handleMenuClick(item)}
          className={active === item ? "active" : ""}
        >
          {item}
        </div>
      ))}
    </div>
  );
}

export default Sidebar;