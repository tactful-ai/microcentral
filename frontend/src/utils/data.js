export const metricsData = [
    {
        name: "CPU Usage",
        type: "integer",
        value: 75,
        weight: 10,
        lastUpdate: "2024-09-01"
    },
    {
        name: "Memory Usage",
        type: "float",
        value: 61.77,
        weight: 60,
        lastUpdate: "2024-09-02"
    },
    {
        name: "Network Latency",
        type: "boolean",
        value: 0,
        weight: 15,
        lastUpdate: "2024-09-03"
    },
    {
        name: "Database Queries",
        type: "boolean",
        value: 1,
        weight: 10,
        lastUpdate: "2024-09-04"
    },
    {
        name: "API Response Time",
        type: "integer",
        value: 45,
        weight: 5,
        lastUpdate: "2024-09-05"
    }
];
export const booleanData = {
    labels: ['2024-09-01', '2024-09-02', '2024-09-03'], 
    datasets: [
      {
        label: 'True',
        data: [10, 15, 8], 
        backgroundColor: 'rgba(54, 162, 235, 0.6)',
      },
      {
        label: 'False',
        data: [5, 7, 12], 
        backgroundColor: 'rgba(255, 99, 132, 0.6)',
      },
    ],
  };
  
export const stringData = {
    labels: ['2024-09-01', '2024-09-02', '2024-09-03', '2024-09-04'],
    datasets: [
        {
            label: 'Category A',
            data: [12, 19, 3, 5], 
            backgroundColor: 'rgba(255, 99, 132, 0.6)',
        },
        {
            label: 'Category B',
            data: [8, 15, 20, 10], 
            backgroundColor: 'rgba(54, 162, 235, 0.6)',
        },
        {
            label: 'Category C',
            data: [5, 10, 15, 22], 
            backgroundColor: 'rgba(75, 192, 192, 0.6)',
        },
    ],
};


export const lineData = {
    labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    datasets: [
      {
        label: "First dataset",
        data: [33, 53, 85, 41, 44, 65],
        fill: true,
        backgroundColor: "rgba(75,192,192,0.2)",
        borderColor: "rgba(75,192,192,1)"
      },
      {
        label: "Second dataset",
        data: [33, 25, 35, 51, 54, 76],
        fill: false,
        borderColor: "#742774"
      }
    ]
  };
