import React, { useState } from 'react';
import Layout from '../layouts/Layout.jsx';
import { Container, Row, Col, Form, Card, ListGroup } from 'react-bootstrap';
import { Line, Bar, Scatter } from 'react-chartjs-2';
import { metricsData, stringData, lineData, booleanData, scatterData } from '../utils/data.js';
import DateTimePicker from '../components/DateTimePicker.jsx';
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    BarElement,
    Title,
    Tooltip,
    Legend,
  } from 'chart.js';
import ScatterChart from '../components/common/ScatterChart.jsx';
  
  ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
    BarElement,
  );


  
const ScorecardMetricRows = ({metricsData, handleDisplay}) => {
    return metricsData.map((metric, index) => (
        <tr key={index}>
            <th scope="row">{index + 1}</th>
            <td>{metric.name}</td>
            <td>{metric.value}</td>
            <td>{metric.weight}</td>
            <td>{metric.lastUpdate}</td>
            <th>
                <button className="action-btn mx-1" onClick={()=>handleDisplay(metric)}>
                    <i className="fa-solid fa-eye"></i>
                </button>
            </th>
        </tr>
    ))
        
};

const InfoCard = ({ serviceName, teamName }) => {
    return (
        <Card style={{ width: '18rem' }}>
            <ListGroup variant="flush">
                <ListGroup.Item>Service Name: {serviceName}</ListGroup.Item>
                <ListGroup.Item>Team Name: {teamName}</ListGroup.Item>
            </ListGroup>
        </Card>
    );
};

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
  
  const stringOptions = (labels=[]) => {
    return ({
        scales: {
            x: {
                type: 'linear',
                position: 'bottom',
                min: 0.00, // Set minimum x value
                max: 10.00, // Set maximum x value
                position: 'bottom',
                ticks: {
                    stepSize: 1, // Ensure the ticks show in steps of 1
                },
            },
            y: {
                type: 'category',
                labels: labels
            }
        },
        plugins: {
            legend: {
              labels: {
                padding: 20, // Add margin or padding to the legend items
              },
            },
        },
    });
  }

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

const GraphController = ({metricType}) => {
    let data = [];
    if (metricType == null) return;
    if (metricType == "integer" || metricType == "float"){
        return <Line data={lineData} options={lineOptions} />;
    }
    else if(metricType == "string") {
        return (
            <div className='h-25'>
                <ScatterChart points={['A', 'C', 'C', 'A', 'B', 'C']} 
                categories={['A', 'B', 'C', 'D']} />
            </div>
        );
    }
    else if(metricType == "boolean") {
        return <Bar data={booleanData} options={booleanOptions} />;
        
    }
}

const ScorecardMetrics = () => {
    const [metricType, setMetricType] = useState(null);

    const handleDisplay = (metric) => {
        console.log(metric);
        setMetricType(metric.type)
    }
      
  return (
    <Layout>
        <Container style={{ color: '#303030 !important' }}>
            <Row className='mt-5 '>
                <Row className="mb-4">
                    <Col xs={7}>
                        <h1 className='mb-3'>Performance</h1>
                        <p className='info-desc w-100'>
                        Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s. when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries.
                        </p>
                    </Col>
                    
                    <Col xs={5} className='text-center px-5'>
                        <InfoCard serviceName={'Visa Auth'} teamName={'Team 1'} />
                    </Col>
                </Row>
                <Row>
                    <Col xs={12}>
                        <table className="table table-striped my-5 mt-2">
                            <thead>
                                <tr>
                                    <th scope="col">#</th>
                                    <th scope="col">Name</th>
                                    <th scope="col">Last Value</th>
                                    <th scope="col">Weight</th>
                                    <th scope="col">Last Update</th>
                                    <th scope="col">Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                <ScorecardMetricRows metricsData={metricsData} 
                                handleDisplay={handleDisplay} />
                            </tbody>
                        </table>
                    </Col>
                </Row>
                <Row>
                    <Col xs={12}>
                        <div className='mx-auto w-50'>
                            <h4>Select data time interval</h4>
                            <DateTimePicker/>
                        </div>
                        <div className='mb-5'>
                            <GraphController metricType={metricType}/>
                        </div>
                    </Col>
                </Row>
            </Row>
        </Container>
    </Layout>
  )
}

export default ScorecardMetrics