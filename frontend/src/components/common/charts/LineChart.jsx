import React from 'react';
import 'chartjs-adapter-date-fns'; 

import { Line } from 'react-chartjs-2';
import { 
    Chart as ChartJS, TimeScale, LinearScale, PointElement, Title, Tooltip, Legend, LineElement 
} from 'chart.js';
ChartJS.register(
  TimeScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
);


const LineChart = ({title, labels, points}) => {
  const lineOptions = {
    scales: {
      x: {
        type: 'time',
        time: {
          unit: 'month',   // Adjust the unit to match your data granularity
          tooltipFormat: 'yyyy-MM-dd HH:mm',  // Format for tooltips
          displayFormats: {
            month: 'MMM yyyy',  // Display format for X-axis labels (e.g., 'Sep 2024')
            day: 'MMM dd',      // Display format for daily data
          }
        },
        title: {
          display: true,
          text: "Time"
        }
      },
      y: {
        title: {
          display: true,
          text: "Value"
        }
      },
    },
    plugins: {
        legend: {
          display: true,
          labels: {
            text: "metric",
            padding: 20,
          },
        },
    },
  }
  const lineData = {
    labels: labels,
    datasets: [
      {
        label: title,
        data: points,
        fill: true,
        backgroundColor: "rgba(75,192,192,0.2)",
        borderColor: "rgba(75,192,192,1)"
      }
    ]
  }

  return (
    <Line data={lineData} options={lineOptions} />
  )
}

export default LineChart