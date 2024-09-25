import React from 'react';
import 'chartjs-adapter-date-fns'; 
import { Bar } from 'react-chartjs-2';
import { 
    Chart as ChartJS, TimeScale, CategoryScale, LinearScale, PointElement, Title, Tooltip, Legend, BarElement 
} from 'chart.js';

ChartJS.register(
    TimeScale,
    CategoryScale,
    LinearScale,
    PointElement,
    Title,
    Tooltip,
    Legend,
    BarElement,
);

const BarChart = ({ title, points }) => {
    // Prepare labels and data from points
    const labels = points.map(point => point.time); // Extract time for labels
    const dataValues = points.map(point => (point.value === 'true' ? 1 : 0)); // Convert value to binary

    const booleanOptions = {
        scales: {
            x: {
                type: 'time',
                time: {
                    minUnit: 'minute',
                    tooltipFormat: 'yyyy MMM dd hh:mm a',
                    displayFormats: {
                        month: 'yyyy MMM',
                        day: 'MMM dd',
                        hour: 'hh a',
                        minute: 'hh:mm a',
                        second: 'mm:ss'
                    }
                },
                ticks: {
                    autoSkip: true,
                    maxTicksLimit: 10,
                },
                grid: {
                    display: true,
                },
                title: {
                    display: true,
                    text: "Time"
                }
            },
            y: {
                min: 0,
                max: 1,
                ticks: {
                    callback: function(value) {
                        // Show only 0 and 1 on the y-axis
                        return (value === 0 || value === 1) ? value : '';
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

    const booleanData = {
        labels: labels,  // Use extracted labels
        datasets: [
            {
                label: title,
                data: dataValues, // Use extracted data values
                backgroundColor: 'rgba(54, 162, 235, 0.6)',
                barThickness: 1,
            },
        ],
    };

    return (
        <Bar data={booleanData} options={booleanOptions} />
    );
}

export default BarChart;
