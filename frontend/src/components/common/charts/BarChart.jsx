import React from 'react'
import { Bar } from 'react-chartjs-2';
import { 
    Chart as ChartJS, CategoryScale, LinearScale, PointElement, Title, Tooltip, Legend, BarElement 
} from 'chart.js';
ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    Title,
    Tooltip,
    Legend,
    BarElement,
);

const BarChart = ({data}) => {
    
const booleanOptions = {
    responsive: true,
    scales: {
      x: {
        title: {
          display: true,
          text: 'Time',
        },
      },
      y: {
        min: 0,
        max: 1,
        ticks: {
            callback: function(value) {
            // Show only 0 and 1 on the y-axis
            if (value === 0 || value === 1) {
                return value;
            }
            return '';
            }
        },
        title: {
          display: true,
          text: 'Value', 
        },
      },
    },
    plugins: {
      legend: {
        position: 'top',
      },
    },
  };

  return (
    <Bar data={data} options={booleanOptions} />
  )
}

export default BarChart