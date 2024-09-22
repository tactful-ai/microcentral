import React from 'react';

import { Line } from 'react-chartjs-2';
import { 
    Chart as ChartJS, CategoryScale, LinearScale, PointElement, Title, Tooltip, Legend, LineElement 
} from 'chart.js';
ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
);


const LineChart = ({data}) => {
    
  const lineOptions = {
    scales: {
        x: {
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
            padding: 20, // Add margin or padding to the legend items
          },
        },
    },
  }
  return (
    <Line data={data} options={lineOptions} />
  )
}

export default LineChart