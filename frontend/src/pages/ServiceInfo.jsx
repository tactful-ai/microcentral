import React, { useEffect, useState } from 'react';
import Layout from '../layouts/Layout.jsx';
import { NavLink, useNavigate, useParams } from 'react-router-dom';
import { Container, Row, Col, Button, Card, Carousel } from 'react-bootstrap';
import { Doughnut } from 'react-chartjs-2';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import { getServiceInfoById } from '../api/services/index.js';

import '../styles/pages/ServiceInfo.css';


ChartJS.register(ArcElement, Tooltip, Legend);

// dummy data for scorecards testing
const scorecards_test = [
  { name: 'Scorecard 1', score: 75.3, lastUpdate: '2024-09-09' },
  { name: 'Scorecard 2', score: 22, lastUpdate: '2024-09-08' },
  { name: 'Scorecard 3', score: 50.9, lastUpdate: '2024-09-07' },
  { name: 'Scorecard 4', score: 99, lastUpdate: '2024-09-06' },
  { name: 'Scorecard 3', score: 73.1, lastUpdate: '2024-09-07' },
  { name: 'Scorecard 4', score: 60, lastUpdate: '2024-09-06' },
];

const ScoreCard = ({ serviceId, id, name, score, lastUpdate }) => {
  const navigate = useNavigate();
  
  const doughnutData = {
    labels: [
      'Score',
      'Loss',
    ],
    datasets: [{
      label: 'value',
      data: [score, 100-score],
      backgroundColor: [
        'rgb(54, 162, 235)',
        'rgb(255, 99, 132)',
      ],
      hoverOffset: 4
    }]
  };

  return (
    <Card className="score-card"
    onClick={()=>navigate(`/dashboard/services/${serviceId}/${id}`)}
    >
      <Card.Body>
        <Card.Title>{name}</Card.Title>
        <Doughnut data={doughnutData} />
        <Card.Text className='mt-3'>Last updated: {lastUpdate}</Card.Text>
      </Card.Body>
    </Card>
  );
};

const ScoreCardCarousel = ({serviceId, scorecards, slideItems}) => {

  const slides = [];
  for (let i = 0; i < scorecards.length; i += slideItems) {
    slides.push(scorecards.slice(i, i + slideItems));
  }

  return (
    <Carousel controls={true} indicators={true} interval={5000} style={{ height: 'auto' }}>
    {slides.map((slide, index) => (
      <Carousel.Item key={index}>
        <Container>
          <Row className="justify-content-center">
            {slide.map((card, idx) => (
              <Col key={card.id} xs={12} sm={6} md={4} className="mb-4">
                <ScoreCard
                  serviceId={serviceId}
                  id={card.id}
                  name={card.name}
                  score={card.score_value}
                  lastUpdate={card.update_time}
                />
              </Col>
            ))}
          </Row>
        </Container>
      </Carousel.Item>
    ))}
  </Carousel>
  );
}

const ServiceInfo = () => {
  const navigate = useNavigate();
  const { service_id } = useParams();

  const [serviceName, setServiceName] = useState('');
  const [serviceDesc, setServiceDesc] = useState('');
  const [serviceTeam, setServiceTeam] = useState('');
  const [serviceScorecards, setServiceScorecards] = useState([]);

  useEffect(() => {
    const fetchService = async () => {
      const service_data = await getServiceInfoById(service_id, navigate);
      setServiceName(service_data.name);
      setServiceTeam(service_data.team_name);
      setServiceDesc(service_data.description);
      setServiceScorecards(service_data.scorecards);
    };
    fetchService();
  }, [service_id]);
  
  return (
    <Layout>
        <Container fluid className="my-5">
        <Row className="mb-3">
          <Col>
            <h1 className='mb-3'>{serviceName}</h1>
            <p className='info-desc'>
              {serviceDesc}
            </p>
          </Col>
        </Row>

        <Row className="my-1">
          <Col>
            <h4>Team Name: {serviceTeam}</h4>
          </Col>
        </Row>

        <Row className="mt-5 mb-4">
          <Col xs={9}>
            <h3>Scorecards List</h3>
          </Col>
          <Col xs={3} className="text-end">
            <NavLink to="/dashboard/services/create" 
              className={( (navData) => navData.isActive? 'active': '')}>
              <Button className="assign-btn">
                Assign New
              </Button>
            </NavLink>
          </Col>
        </Row>
        <Row>
          <ScoreCardCarousel serviceId={service_id}
          scorecards={serviceScorecards} slideItems={3} />
        </Row>
        </Container>
    </Layout>
  );
};

export default ServiceInfo;
