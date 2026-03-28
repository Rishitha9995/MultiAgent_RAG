import React, { useState } from "react";

function DocumentCard({ doc }) {

  const [open, setOpen] = useState(false);

  return (
    <div className="doc-card" onClick={() => setOpen(!open)}>
      <div className="doc-title">{doc.source}</div>

      {open && (
        <div className="doc-content">
          <p><strong>Score:</strong> {doc.score}</p>
          <p><strong>Reason:</strong> {doc.reason}</p>
        </div>
      )}
    </div>
  );
}

export default DocumentCard;