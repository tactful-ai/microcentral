import React from 'react';
import Layout from '../layouts/Layout.jsx';
import { NavLink } from 'react-router-dom';
import { Container, Row, Col, Form, Card, ListGroup } from 'react-bootstrap';
import { Line } from 'react-chartjs-2';
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
  } from 'chart.js';
  
  ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
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
                <button className="action-btn mx-1" onClick={()=>handleDisplay(metricsData)}>
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

const ScorecardMetrics = () => {
    const metricsData = [
        {
            name: "CPU Usage",
            value: 75,
            weight: 50,
            lastUpdate: "2024-09-01"
        },
        {
            name: "Memory Usage",
            value: 60,
            weight: 70,
            lastUpdate: "2024-09-02"
        },
        {
            name: "Network Latency",
            value: 30,
            weight: 80,
            lastUpdate: "2024-09-03"
        },
        {
            name: "Database Queries",
            value: 90,
            weight: 60,
            lastUpdate: "2024-09-04"
        },
        {
            name: "API Response Time",
            value: 45,
            weight: 90,
            lastUpdate: "2024-09-05"
        }
    ];
    

    const lineData = {
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

    const handleDisplay = (metricsData) => {
        console.log("display");
        console.log(metricsData)
    }

      
  return (
    <Layout>
        <Container style={{ color: '#303030 !important' }}>
            <Row className='mt-5 '>
                <Col lg={6}>
                    <Row className="mb-3">
                        <Col xs={12}>
                            <h1 className='mb-3'>Performance</h1>
                            <p className='info-desc w-100'>
                            Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s. when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries.
                            </p>
                        </Col>
                        <Col xs={12}>
                        <table className="table table-striped my-4">
                            <thead>
                                <tr>
                                    <th scope="col">#</th>
                                    <th scope="col">Name</th>
                                    <th scope="col">Value</th>
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
                </Col>
                <Col lg={6} className='px-5'>
                    <Row className='text-center vh-100'>
                        <Col xs={12}>
                            <InfoCard serviceName={'Visa Auth'} teamName={'Team 1'} />
                        </Col>
                        <Col xs={12}>
                            <Form.Control type="text" placeholder="Enter Interval" 
                            className='mb-4' />
                            <Line data={lineData} />
                        </Col>
                    </Row>
                </Col>
            </Row>
        </Container>
    </Layout>
  )
}

export default ScorecardMetrics