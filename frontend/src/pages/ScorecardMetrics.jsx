import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { Container, Row, Col, Form, Card, ListGroup } from 'react-bootstrap';
import Layout from '../layouts/Layout.jsx';
import DateTimePicker from '../components/DateTimePicker.jsx';

import ScatterChart from '../components/common/charts/ScatterChart.jsx';
import LineChart from '../components/common/charts/LineChart.jsx';
import BarChart from '../components/common/charts/BarChart.jsx';

import { getMetricById, getMetricReadings, getScorecardById, getServiceById, getServiceMetricInfo } from '../api/services/index.js';

const ScorecardMetricRows = ({metricsData, handleDisplay}) => {
    return (
        <>
            {metricsData && metricsData.length > 0 && metricsData.map((metric, index) => (
                <tr key={index}>
                    <th scope="row">{metric.metricId}</th>
                    <td>{metric.metricName}</td>
                    <td>
                        {
                            metric.value === true ? '1' :
                            metric.value === false ? '0' : metric.value
                        }
                    </td>
                    <td>{metric.weight}</td>
                    <td>{metric.timestamp}</td>
                    <th>
                        <button className="action-btn mx-1" onClick={() => handleDisplay(metric)}>
                            <i className="fa-solid fa-eye"></i>
                        </button>
                    </th>
                </tr>
            ))}
        </>
    );
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

const ChartController = ({title, metricType, labels, points}) => {
    if (metricType == null) return;
    if (metricType == "integer" || metricType == "float"){
        return <LineChart title={title} labels={labels} points={points} />;
    }
    else if(metricType == "string") {
        return (
            <ScatterChart title={title} points={points} />
        );
    }
    else if(metricType == "boolean") {
        return <BarChart title={title} labels={labels} points={points} />;
    }
}

const ScorecardMetrics = () => {
    const {service_id, scorecard_id} = useParams();
    const [metricType, setMetricType] = useState(null);
    
    const [serviceTeam, setServiceTeam] = useState()
    const [serviceName, setServiceName] = useState('');
    const [serviceMetrics, setServiceMetrics] = useState([]);
    const [scorecardName, setScorecardName] = useState('');
    const [scorecardDesc, setScorecardDesc] = useState('');

    const [startDate, setStartDate] = useState('');
    const [endDate, setEndDate] = useState('');

    const [labels, setLabels] = useState([]);
    const [points, setPoints] = useState([]);

    const handleDisplay = async (metric) => {
        const metric_data = await getMetricById(metric.metricId);
        const metric_readings = await getMetricReadings(service_id, startDate, endDate);
        const selected_readings = metric_readings.filter(
            reading => reading.metricId == metric.metricId
        );
        setLabels([]); 
        setPoints([]); 

        const newLabels = selected_readings.map(reading => reading.timestamp);
        const newPoints = selected_readings.map(reading => 
            ({ time: reading.timestamp, value: reading.value })
        );

        setLabels(newLabels);
        setPoints(newPoints);


        setMetricType(metric_data.type);
        console.log("metric readings: ", selected_readings);
        console.log('start date: ', startDate, ', end date: ', endDate)
        console.log('labels: ', labels, ', points: ', points)
    }
    
  useEffect(() => {
    const fetchScorecardInfo = async () => {
        const scorecard_data = await getScorecardById(scorecard_id);
        const service = await getServiceById(service_id);
        const service_metrics = await getServiceMetricInfo(service_id, scorecard_id);

        setServiceName(service.name)
        setServiceTeam(service.team_name)
        setServiceMetrics(service_metrics);

        setScorecardName(scorecard_data.name);
        setScorecardDesc(scorecard_data.description);
    };
    fetchScorecardInfo();
  }, [scorecard_id]);


  return (
    <Layout>
        <Container>
            <Row className='mt-5 '>
                <Row className="mb-4">
                    <Col xs={7}>
                        <h1 className='mb-3'>{scorecardName}</h1>
                        <p className='info-desc w-100'>
                            {scorecardDesc}
                        </p>
                    </Col>
                    
                    <Col xs={5} className='text-center px-5'>
                        <InfoCard serviceName={serviceName} teamName={serviceTeam} />
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
                                <ScorecardMetricRows metricsData={serviceMetrics} 
                                handleDisplay={handleDisplay} />
                            </tbody>
                        </table>
                    </Col>
                </Row>
                <Row>
                    <Col xs={12}>
                        <div className='mx-auto w-50'>
                            <h4>Select data time interval</h4>
                            <DateTimePicker onStartDateChange={setStartDate} 
                            onEndDateChange={setEndDate}/>
                        </div>
                        <div className='mb-5'>
                            <ChartController metricType={metricType}
                            title={metricType} labels={labels} 
                            points={points} />
                        </div>
                    </Col>
                </Row>
            </Row>
        </Container>
    </Layout>
  )
}

export default ScorecardMetrics