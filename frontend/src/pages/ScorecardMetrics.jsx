import React, { useState, useEffect } from 'react';
import { Container, Row, Col, Form, Card, ListGroup } from 'react-bootstrap';
import Layout from '../layouts/Layout.jsx';
import DateTimePicker from '../components/DateTimePicker.jsx';

import ScatterChart from '../components/common/charts/ScatterChart.jsx';
import LineChart from '../components/common/charts/LineChart.jsx';
import BarChart from '../components/common/charts/BarChart.jsx';

import { metricsData, stringData, lineData, booleanData, scatterData } from '../utils/data.js';
import { getMetricById, getMetricReadings, getScorecardById } from '../api/services/index.js';
import { useParams } from 'react-router-dom';

const ScorecardMetricRows = ({metricsData, handleDisplay}) => {
    console.log(metricsData)
    return metricsData.map((metric, index) => (
        <tr key={index}>
            <th scope="row">{metric.id}</th>
            <td>{metric.name}</td>
            <td>{
                metric.desiredValue == true ? '1':
                metric.desiredValue == false ? '0': metric.desiredValue
            }</td>
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
    const {scorecard_id} = useParams();
    const [metricType, setMetricType] = useState(null);
    
    const [scorecardName, setScorecardName] = useState('');
    const [scorecardDesc, setScorecardDesc] = useState('');
    const [scorecardMetrics, setScorecardMetrics] = useState([]);
    const [scorecardTeam, setScorecardTeam] = useState('');

    const handleDisplay = async (metric) => {
        console.log(metric);
        setMetricType(metric.type);
        // const data = await getMetricReadings(1, '', '');
        // console.log(data)
    }
    
  useEffect(() => {
    const fetchScorecardInfo = async () => {
        const scorecard_data = await getScorecardById(scorecard_id);
        // scorecard_data.metrics.map(async(metric)=>{
        //     const true_metric = await getMetricById(metric.id);
        //     metric.name = true_metric.name;
        //     metric.type = true_metric.type;
        // })
        setScorecardName(scorecard_data.name);
        setScorecardDesc(scorecard_data.description);
        setScorecardMetrics(scorecard_data.metrics);
        setScorecardTeam(scorecard_data.team_name);
    };
    fetchScorecardInfo();
  }, [scorecard_id]);
      
  return (
    <Layout>
        <Container style={{ color: '#303030 !important' }}>
            <Row className='mt-5 '>
                <Row className="mb-4">
                    <Col xs={7}>
                        <h1 className='mb-3'>{scorecardName}</h1>
                        <p className='info-desc w-100'>
                            {scorecardDesc}
                        </p>
                    </Col>
                    
                    <Col xs={5} className='text-center px-5'>
                        <InfoCard serviceName={'Visa Auth'} teamName={scorecardTeam} />
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
                                <ScorecardMetricRows metricsData={scorecardMetrics} 
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