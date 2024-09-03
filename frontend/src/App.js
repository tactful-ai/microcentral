import React from 'react';
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import MetricCreateEdit from './pages/MetricCreateEdit';
import Services from './pages/Services.jsx';
import Metrics from './pages/Metrics';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Services />}/>
        <Route path="/dashboard/services" element={<Services />}/>
        <Route path="/dashboard/metrics" element={<Metrics />}/>
        <Route path="/dashboard/metrics/create" element={<MetricCreateEdit mode="create"/>}/>
        <Route path="/dashboard/metrics/view/:metric_id" element={<MetricCreateEdit mode="view"/>}/>
        <Route path="/dashboard/metrics/edit/:metric_id" element={<MetricCreateEdit mode="edit"/>}/>
        {/* <Route element={"404 Not Found"} />*/} 
      </Routes>
    </BrowserRouter>
  );
}

export default App;
