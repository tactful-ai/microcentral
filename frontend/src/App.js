import React from 'react';
import {BrowserRouter, Routes, Route, Navigate} from 'react-router-dom';
import MetricCreateEdit from './pages/MetricCreateEdit';
import Services from './pages/Services.jsx';
import ServiceInfo from './pages/ServiceInfo.jsx';
import Metrics from './pages/Metrics';
import NotFound from './pages/NotFound';
import Scorecards from './pages/Scorecards';
import ScorecardCreateEdit from './pages/ScorecardCreateEdit.jsx';
import ServiceCreateEdit from './pages/ServiceCreateEdit';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/dashboard/services" />}/>
        <Route path="/dashboard/services" element={<Services />}/>
        <Route path="/dashboard/services/:service_id" element={<ServiceInfo />}/>
        <Route path="/dashboard/services/create" element={<ServiceCreateEdit />}/>
        <Route path="/dashboard/metrics" element={<Metrics />}/>
        <Route path="/dashboard/scorecards" element={<Scorecards />}/>
        <Route path="/dashboard/scorecards/create" element={<ScorecardCreateEdit mode="create" />}/>
        <Route path="/dashboard/scorecards/edit/:scorecard_id" element={<ScorecardCreateEdit mode="edit" />}/>
        <Route path="/dashboard/metrics/create" element={<MetricCreateEdit mode="create"/>}/>
        <Route path="/dashboard/metrics/view/:metric_id" element={<MetricCreateEdit mode="edit"/>}/>
        <Route path="/dashboard/metrics/edit/:metric_id" element={<MetricCreateEdit mode="edit"/>}/>
        <Route path="/404" element={<NotFound />} /> 
        <Route path="*" element={<NotFound />} /> 
      </Routes>
    </BrowserRouter>
  );
}

export default App;
