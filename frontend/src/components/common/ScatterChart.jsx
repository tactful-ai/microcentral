import React from 'react'
import { Scatter } from 'react-chartjs-2';

const ScatterChart = ({ categories, points }) => {
    const stringOptions = {
      scales: {
        x: {
          type: 'linear',
          position: 'bottom',
          min: 0.00, // Set minimum x value
          max: 10.00, // Set maximum x value
          ticks: {
            stepSize: 1, // Ensure the ticks show in steps of 1
          },
          title: {
            display: true,
            text: 'Time',
          },
        },
        y: {
          type: 'category',
          labels: categories,
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
            padding: 20, // Add margin or padding to the legend items
          },
        },
      },
    };
  
    const scatterData = {
      labels: ['1.00', '2.00', '3.00', '4.00', '5.00', '6.00', '7.00', '8.00', '9.00', '10.00'],
      datasets: [
        {
          label: 'Scatter Dataset',
          data: points.map((point, index) => {
            const yValue = categories.indexOf(point);
            // Log points and yValue for debugging
            console.log(`Point: ${point}, Index: ${index}, yValue: ${yValue}`);
            return {
              x: index + 1,
              y: yValue === -1 ? null : yValue,
            };
          }),
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
  

export default ScatterChart