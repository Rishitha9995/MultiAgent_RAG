import React from "react";
import { Bar } from "react-chartjs-2";

function MetricsPanel({ metrics }) {

  const chartData = metrics?.metrics && {
    labels: Object.keys(metrics.metrics),
    datasets: [{
      label: "Metrics",
      data: Object.values(metrics.metrics)
    }]
  };

  return (
    <div className="metrics-panel">
      <h3>Metrics</h3>

      {chartData ? (
        <>
          <Bar data={chartData} />
          <p>Response Time: {metrics.response_time}s</p>
        </>
      ) : (
        <p>No data</p>
      )}
    </div>
  );
}

export default MetricsPanel;