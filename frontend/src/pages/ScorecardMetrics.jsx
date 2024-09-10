import React from 'react';
import Layout from '../layouts/Layout.jsx';
import { NavLink } from 'react-router-dom';
import { Container, Row, Col, Button, Card, ListGroup } from 'react-bootstrap';
import { Doughnut } from 'react-chartjs-2';
import { Chart as ChartJS } from 'chart.js';


const ScorecardMetricRows = (props) => {
    return props.metricsData.map((metric, index) => (
        <tr key={index}>
            <th scope="row">{index + 1}</th>
            <td>{metric.name}</td>
            <td>{metric.value}</td>
            <td>{metric.weight}</td>
            <td>{metric.lastUpdate}</td>
            <th>
                <button className="action-btn mx-1">
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
    

  return (
    <Layout>
        <Container style={{ color: '#303030 !important' }}>
            <Row className='mt-5 '>
                <Col xs={7}>
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
                                <ScorecardMetricRows metricsData={metricsData} />
                            </tbody>
                        </table>
                        </Col>
                    </Row>
                </Col>
                <Col xs={5}>
                    <Row className='text-center'>
                        <Col xs={12}>
                            <InfoCard serviceName={'Visa Auth'} teamName={'Team 1'} />
                        </Col>
                        <Col xs={12}>

                        </Col>
                    </Row>
                </Col>
            </Row>
        </Container>
    </Layout>
  )
}

export default ScorecardMetrics