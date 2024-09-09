import React from 'react';
import Layout from '../layouts/Layout.jsx';
import { NavLink } from 'react-router-dom';
import { Container, Row, Col, Button, Card, Image } from 'react-bootstrap';
import { Doughnut } from 'react-chartjs-2';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import '../styles/pages/ServiceInfo.css';

ChartJS.register(ArcElement, Tooltip, Legend);

const TeamMember = ({ image }) => (
  <div className="team-member m-1">
    
  </div>
);

const ScoreCard = ({ name, score, lastUpdate }) => {
  
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
    <Card className="score-card">
      <Card.Body>
        <Card.Title>{name}</Card.Title>
        <Doughnut data={doughnutData} />
        <Card.Text className='mt-3'>Last updated: {lastUpdate}</Card.Text>
      </Card.Body>
    </Card>
  );
};

const ServiceInfo = () => {
  return (
    <Layout>
        <Container fluid className="my-5">
        <Row className="mb-3">
            <Col>
                <h1 className='mb-3'>Performance</h1>
                <p className='info-desc'>
                Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages.
                </p>
            </Col>
        </Row>

        <Row className="my-1">
            <Col>
                <h2>Team Members</h2>
                <div className="d-flex">
                    <TeamMember image="../assets/member1.jpg" />
                    <TeamMember image="../assets/member1.jpg" />
                    <TeamMember image="../assets/member1.jpg" />
                    <Button variant="secondary" className="member-more m-1">
                        <i class="bi bi-three-dots"></i>
                    </Button>
                </div>
            </Col>
        </Row>

        <Row className="mt-5 mb-4">
            <Col xs={9}>
                <h2>Scorecards List</h2>
            </Col>
            <Col xs={3} className="text-end">
              <NavLink to="/dashboard/scorecards/create" 
                className={( (navData) => navData.isActive? 'active': '')}>
                <Button className="assign-btn">
                  Assign New
                </Button>
              </NavLink>
            </Col>
        </Row>
        <Row>
            <Col md={4}>
              <ScoreCard name="Scorecard 1" score={75.4} lastUpdate="2024-09-09" />
            </Col>
            <Col md={4}>
              <ScoreCard name="Scorecard 2" score={85} lastUpdate="2024-09-08" />
            </Col>
            <Col md={4}>
              <ScoreCard name="Scorecard 3" score={33.6} lastUpdate="2024-09-07" />
            </Col>
        </Row>
        </Container>
    </Layout>
  );
};

export default ServiceInfo;
