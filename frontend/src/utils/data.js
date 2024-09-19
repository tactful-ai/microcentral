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
        type: "string",
        value: "test",
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

export const servicesData = [
    {
        id: '1',
        name: 'Service A',
        description: 'A comprehensive service for managing financial transactions.',
        type: 'Financial',
        area: ['North America', 'Europe']
    },
    {
        id: '2',
        name: 'Service B',
        description: 'A service specializing in data analytics and business intelligence.',
        type: 'Analytics',
        area: ['Asia', 'Australia']
    },
    {
        id: '3',
        name: 'Service C',
        description: 'Provides cloud computing resources and support.',
        type: 'Cloud Computing',
        area: ['South America', 'Africa']
    },
    {
        id: '4',
        name: 'Service D',
        description: 'An advanced service for digital marketing and SEO.',
        type: 'Marketing',
        area: ['Middle East', 'Asia']
    },
    {
        id: '5',
        name: 'Service E',
        description: 'Offers cybersecurity solutions and support.',
        type: 'Security',
        area: ['Europe', 'North America']
    }
];

export const booleanData = {
    labels: ['1.00', '2.00', '3.00', '4.00', '5.00', '6.00', '7.00', '8.00', '9.00', '10.00'], 
    datasets: [
      {
        label: 'True',
        data: [0, 1, 1, 1, 0, 1, 0, 0, 0, 1], 
        backgroundColor: 'rgba(54, 162, 235, 0.6)',
        barThickness: 1
      },
    ],
  };
  
export const scatterData = (points) => {
    let categories = ['A', 'B', 'C'];
    return ({
        categories: categories,
        labels: ['1.00', '2.00', '3.00', '4.00', '5.00', '6.00', '7.00', '8.00', '9.00', '10.00'],
        datasets: [
            {
                label: 'Scatter Dataset',
                data: points.map((point, index) => ({
                    x: index+1,  // x is constant since we want to display rectangles aligned vertically
                    y: categories.indexOf(point), // map data to the index of the category
                })),
                backgroundColor: 'rgba(75, 192, 192, 0.6)',
                pointStyle: 'rect', // Use 'rect' to display rectangles
                pointRadius: 10,    // Radius of the rectangle (size)
            },
        ],
    })
}

export const stringData = {
    labels: ['1.00', '2.00', '3.00', '4.00', '5.00', '6.00', '7.00', '8.00', '9.00', '10.00'],
    categories: ['A', 'B', 'C', 'D'],
    datasets: [
        {
            data: [''], 
            backgroundColor: 'rgba(255, 99, 132, 0.6)',
        },
        {
            label: 'Category B',
            data: [''], 
            backgroundColor: 'rgba(54, 162, 235, 0.6)',
        },
        {
            label: 'Category C',
            data: [''], 
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
    //   {
    //     label: "Second dataset",
    //     data: [33, 25, 35, 51, 54, 76],
    //     fill: false,
    //     borderColor: "#742774"
    //   }
    ]
  };
