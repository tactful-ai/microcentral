import React, { useState } from 'react';
import { Container, Row, Col, Form, Card, ListGroup } from 'react-bootstrap';
import Layout from '../layouts/Layout.jsx';
import DateTimePicker from '../components/DateTimePicker.jsx';

import ScatterChart from '../components/common/charts/ScatterChart.jsx';
import LineChart from '../components/common/charts/LineChart.jsx';
import BarChart from '../components/common/charts/BarChart.jsx';

import { metricsData, stringData, lineData, booleanData, scatterData } from '../utils/data.js';
import { getMetricReadings } from '../api/services/index.js';

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

const GraphController = ({metricType}) => {
    if (metricType == null) return;
    if (metricType == "integer" || metricType == "float"){
        return <LineChart data={lineData} />;
    }
    else if(metricType == "string") {
        return (
            <ScatterChart points={['A', 'C', 'C', 'A', 'B', 'C']} 
            categories={['A', 'B', 'C', 'D']} />
        );
    }
    else if(metricType == "boolean") {
        return <BarChart data={booleanData} />;
    }
}

const ScorecardMetrics = () => {
    const [metricType, setMetricType] = useState(null);

    const handleDisplay = async (metric) => {
        console.log(metric);
        setMetricType(metric.type);
        const data = await getMetricReadings(1, '', '');
        console.log(data)
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