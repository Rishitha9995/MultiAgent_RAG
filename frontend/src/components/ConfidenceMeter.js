import React from "react";

function ConfidenceMeter({ level }) {

  const getColor = () => {
    if (level === "High") return "#22c55e";
    if (level === "Medium") return "#f59e0b";
    return "#ef4444";
  };

  const getWidth = () => {
    if (level === "High") return "90%";
    if (level === "Medium") return "60%";
    return "30%";
  };

  return (
    <div className="confidence-box">
      <div className="confidence-label">Confidence: {level}</div>
      <div className="confidence-bar">
        <div
          className="confidence-fill"
          style={{
            width: getWidth(),
            background: getColor()
          }}
        />
      </div>
    </div>
  );
}

export default ConfidenceMeter;