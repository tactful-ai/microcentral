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

const ScatterChart = ({ title, points }) => {
  // Extract unique categories from the points
  const categories = [...new Set(points.map(point => point.value))].sort();

  // Chart.js options
  const scatterOptions = {
    responsive: true,
    scales: {
        x: {
            type: 'time',
            time: {
                tooltipFormat: 'yyyy MMM dd hh:mm a', // Tooltip format with AM/PM
                displayFormats: {
                  hour: 'MMM dd, hh a', // Display format for hour
                    day: 'MMM dd',
                },
            },
            ticks: {
                maxTicksLimit: 10, // Limit the number of ticks on the x-axis
            },
            title: {
              display: true,
              text: 'Time',
            },
        },
        y: {
            type: 'category',
            title: {
              display: true,
              text: 'Categories',
            },
            labels: categories, // Display the unique categories on the y-axis
        },
    },
    plugins: {
        legend: {
          position: 'top',
        },
    },
};

  // Helper function to get mapped points
  const mapPoints = () => {
      return points.map(point => {
          const categoryIndex = categories.indexOf(point.value);
          return {
              x: new Date(point.time), // Use ISO time for x value
              y: categoryIndex !== -1 ? categories[categoryIndex] : 'Unknown', // Map to category
          };
      });
  };

  // Dataset for the scatter chart
  const scatterData = {
      datasets: [
          {
              label: title,
              data: mapPoints(), // Map points to x,y format
              backgroundColor: points.map(point => {
                  const categoryIndex = categories.indexOf(point.value);
                  const colors = [
                      'rgba(255, 99, 132, 0.6)',
                      'rgba(54, 162, 235, 0.6)',
                      'rgba(255, 206, 86, 0.6)',
                      'rgba(75, 192, 192, 0.6)',
                      'rgba(153, 102, 255, 0.6)',
                      'rgba(255, 159, 64, 0.6)',
                      'rgba(201, 203, 207, 0.6)',
                  ];
                  return categoryIndex === -1 ? 'rgba(0, 0, 0, 0.1)' : 
                  colors[categoryIndex % colors.length];
              }),
              pointStyle: 'rect',
              pointRadius: 10,
          },
      ],
  };

  return <Scatter data={scatterData} options={scatterOptions} />;
};

export default ScatterChart;


