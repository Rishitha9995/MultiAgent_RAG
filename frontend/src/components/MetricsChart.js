import React from "react";
import { Pie } from "react-chartjs-2";
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend
} from "chart.js";

ChartJS.register(ArcElement, Tooltip, Legend);

function MetricsChart({ metrics }) {

  if (!metrics) return null;

  const chartData = {
    labels: [
      "Answer Match",
      "Query Relevance",
      "Context Coverage"
    ],
    datasets: [
      {
        data: [
          metrics["Answer-Context Similarity"],
          metrics["Query-Context Relevance"],
          metrics["Context Coverage"]
        ],
        backgroundColor: [
          "#1e3a8a",
          "#3b82f6",
          "#93c5fd"
        ],
        borderWidth: 1
      }
    ]
  };

  const options = {
    plugins: {
      tooltip: {
        callbacks: {
          label: function (context) {
            return `${context.label}: ${(context.raw * 100).toFixed(1)}%`;
          }
        }
      },
      legend: {
        position: "bottom"
      }
    }
  };

  return (
    <div style={{ width: "260px", margin: "auto" }}>
      <Pie data={chartData} options={options} />
    </div>
  );
}

export default MetricsChart;