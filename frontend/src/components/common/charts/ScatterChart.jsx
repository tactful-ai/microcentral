import React from 'react'
import { Scatter } from 'react-chartjs-2';
import { 
    Chart as ChartJS, CategoryScale, LinearScale, PointElement, Title, Tooltip, Legend
} from 'chart.js';
ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    Title,
    Tooltip,
    Legend,
);

const ScatterChart = ({ categories, points }) => {
  // Chart.js options
  const stringOptions = {
    scales: {
      x: {
        type: 'linear', // Keep linear for numerical values, or 'time' if using time data
        position: 'bottom',
        min: 0.00,
        max: 10.00,
        ticks: {
          stepSize: 1,
        },
        title: {
          display: true,
          text: 'Time',
        },
      },
      y: {
        type: 'category', // Using category for categorical data
        labels: categories, // Your list of categories
        title: {
          display: true,
          text: 'Label',
        },
      },
    },
    plugins: {
      legend: {
        display: false,
        labels: {
          padding: 20,
        },
      },
    },
  };

  // Helper function to get points
  const mapPoints = () => {
    let mappedPoints = [];
    points.map((point, index) => {
      const yValue = categories.indexOf(point.category);
      mappedPoints.push({
        x: index + 1, 
        y: point
      });
    });
    return mappedPoints;
  };

  // Dataset for the scatter chart
  const scatterData = {
    datasets: [
      {
        label: 'Scatter Dataset',
        data: mapPoints(),
        backgroundColor: points.map(point => {
          const categoryIndex = categories.indexOf(point);
          const colors = [
            'rgba(255, 99, 132, 0.6)',
            'rgba(54, 162, 235, 0.6)',
            'rgba(255, 206, 86, 0.6)',
            'rgba(75, 192, 192, 0.6)',
            'rgba(153, 102, 255, 0.6)',
            'rgba(255, 159, 64, 0.6)',
            'rgba(201, 203, 207, 0.6)',
          ];
          return categoryIndex === -1 ? 'rgba(0, 0, 0, 0.1)' : colors[categoryIndex % colors.length];
        }),
        pointStyle: 'rect',
        pointRadius: 10,
      },
    ],
  };

  return <Scatter data={scatterData} options={stringOptions} />;
};

export default ScatterChart;


