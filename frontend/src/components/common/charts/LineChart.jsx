import React from 'react';
import 'chartjs-adapter-date-fns'; 

import { Line } from 'react-chartjs-2';
import { 
    Chart as ChartJS, TimeScale, CategoryScale, LinearScale, PointElement, Title, Tooltip, Legend, LineElement 
} from 'chart.js';

ChartJS.register(
    TimeScale,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
);

const LineChart = ({ title, points }) => {
    // Prepare labels and data from points
    const labels = points.map(point => point.time); // Extract time for labels
    const dataValues = points.map(point => point.value); // Extract values for the y-axis

    const lineOptions = {
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
    };

    const lineData = {
        labels: labels,
        datasets: [
            {
                label: title,
                data: dataValues, // Use extracted data values
                fill: true,
                backgroundColor: "rgba(75,192,192,0.2)",
                borderColor: "rgba(75,192,192,1)"
            }
        ]
    };

    return (
        <Line data={lineData} options={lineOptions} />
    );
}

export default LineChart;
