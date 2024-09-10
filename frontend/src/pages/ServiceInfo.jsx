import React from 'react';
import Layout from '../layouts/Layout.jsx';
import { NavLink, useNavigate } from 'react-router-dom';
import { Container, Row, Col, Button, Card, Carousel } from 'react-bootstrap';
import { Doughnut } from 'react-chartjs-2';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import '../styles/pages/ServiceInfo.css';
ChartJS.register(ArcElement, Tooltip, Legend);



const scorecards = [
  { name: 'Scorecard 1', score: 75.3, lastUpdate: '2024-09-09' },
  { name: 'Scorecard 2', score: 22, lastUpdate: '2024-09-08' },
  { name: 'Scorecard 3', score: 50.9, lastUpdate: '2024-09-07' },
  { name: 'Scorecard 4', score: 99, lastUpdate: '2024-09-06' },
  { name: 'Scorecard 3', score: 73.1, lastUpdate: '2024-09-07' },
  { name: 'Scorecard 4', score: 60, lastUpdate: '2024-09-06' },
];


const TeamMember = ({ image }) => (
  <div className="team-member m-1">
    
  </div>
);

const ScoreCard = ({ name, score, lastUpdate }) => {
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
    onClick={()=>navigate('/dashboard/services/1/10')}
    >
      <Card.Body>
        <Card.Title>{name}</Card.Title>
        <Doughnut data={doughnutData} />
        <Card.Text className='mt-3'>Last updated: {lastUpdate}</Card.Text>
      </Card.Body>
    </Card>
  );
};

const ScoreCardCarousel = ({scorecards, slideItems}) => {

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
              <Col key={idx} xs={12} sm={6} md={4} className="mb-4">
                <ScoreCard
                  name={card.name}
                  score={card.score}
                  lastUpdate={card.lastUpdate}
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

  return (
    <Layout>
        <Container fluid className="my-5">
        <Row className="mb-3">
          <Col>
            <h1 className='mb-3'>Visa Auth</h1>
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
          <ScoreCardCarousel scorecards={scorecards} slideItems={3} />
        </Row>
        </Container>
    </Layout>
  );
};

export default ServiceInfo;
