import React, { useState } from "react";
import MetricsChart from "./MetricsChart";
import DocumentCard from "./DocumentCard";
import Pipeline from "./Pipeline";


function Message({ msg }) {
  const [showOptions, setShowOptions] = useState(false);

  if (msg.type === "user") {
    return <div className="user-msg">{msg.text}</div>;
  }

  if (msg.loading) {
    return (
      <div className="ai-msg">
        <Pipeline loading={true} />
      </div>
    );
  }

  const answerSteps = msg.answer?.split("•").filter((p) => p.trim());

  const copyFull = () => {
    navigator.clipboard.writeText(msg.answer);
    setShowOptions(false);
  };

  const copyAnswerOnly = () => {
    navigator.clipboard.writeText(answerSteps.join("\n"));
    setShowOptions(false);
  };

  return (
    <div className="ai-msg">
      {/* ANSWER AS STEPS */}
      <div className="section-card">
        <h4>Final Answer</h4>
        <ul>
          {answerSteps.map((p, i) => (
            <li key={i}>{p}</li>
          ))}
        </ul>
      </div>

      {/* DOCUMENTS */}
      <div className="section-card">
        <h4>Top Retrieved Documents</h4>
        {msg.explanations?.map((doc, i) => (
          <DocumentCard key={i} doc={doc} />
        ))}
      </div>

      {/* METRICS */}
      <div className="section-card">
        <h4>RAG Metrics</h4>

        {/* CONFIDENCE */}
        <div className="confidence-text">
          Confidence: <strong>{msg.metrics?.["Confidence Level"]}</strong>
        </div>

        {/* CHART */}
        <MetricsChart metrics={msg.metrics} />

        {/* PERCENT TEXT (CLEAN) */}
        <div className="metrics-list">
          <div>
            Answer Match:{" "}
            {(msg.metrics["Answer-Context Similarity"] * 100).toFixed(1)}%
          </div>
          <div>
            Query Relevance:{" "}
            {(msg.metrics["Query-Context Relevance"] * 100).toFixed(1)}%
          </div>
          <div>
            Context Coverage:{" "}
            {(msg.metrics["Context Coverage"] * 100).toFixed(1)}%
          </div>
        </div>

        {/* RESPONSE TIME */}
        <div className="response-time">⏱ {msg.response_time}s</div>
      </div>

      {/* COPY */}
      <div className="copy-container bottom-copy">
        <button
          className="copy-btn"
          onClick={() => setShowOptions(!showOptions)}
        >
          <img src="https://img.icons8.com/ios-glyphs/30/000000/copy.png" alt="Copy" />
        </button>

        {showOptions && (
          <div className="copy-dropdown">
            <div onClick={copyFull}>Copy full</div>
            <div onClick={copyAnswerOnly}>Copy answer</div>
          </div>
        )}
      </div>
    </div>
  );
}

export default Message;
