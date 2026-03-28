// import React from "react";

// function Pipeline({ activeAgent }) {
//   const agents = [
//     "Query Agent",
//     "Router Agent",
//     "Retriever",
//     "Reasoning",
//     "Formatter",
//   ];

//   return (
//     <div className="pipeline-container">
//       <div className="pipeline">
//         {agents.map((agent, index) => (
//           <React.Fragment key={index}>
//             <div
//               className={`agent ${activeAgent === agent ? "active" : ""}`}
//             >
//               {agent}
//             </div>
//             {index < agents.length - 1 && <div className="arrow">→</div>}
//           </React.Fragment>
//         ))}
//       </div>
//       <div className="thinking">Processing agents...</div>
//     </div>
//   );
// }

// export default Pipeline;

import React, { useState, useEffect } from "react";

function Pipeline({ loading }) {
  const agents = [
    "Query Agent",
    "Router Agent",
    "Retriever",
    "Reasoning",
    "Formatter",
  ];
  const [activeIndex, setActiveIndex] = useState(0);

  useEffect(() => {
    if (!loading) return;

    const agents = [
      "Query Agent",
      "Router Agent",
      "Retriever",
      "Reasoning",
      "Formatter",
    ];
    let index = 0;

    const interval = setInterval(() => {
      index += 1;
      if (index >= agents.length) {
        clearInterval(interval);
      } else {
        setActiveIndex(index);
      }
    }, 1000);

    // Start with the first agent active
    setActiveIndex(0);

    return () => clearInterval(interval);
  }, [loading]);

  return (
    <div className="pipeline-container">
      <div className="pipeline">
        {agents.map((agent, index) => (
          <React.Fragment key={index}>
            <div className={`agent ${index === activeIndex ? "active" : ""}`}>
              {agent}
            </div>
            {index < agents.length - 1 && <div className="arrow">→</div>}
          </React.Fragment>
        ))}
      </div>
      {loading && <div className="thinking">Processing agents...</div>}
    </div>
  );
}

export default Pipeline;
