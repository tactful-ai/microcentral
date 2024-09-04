import React, { useEffect, useState, useRef } from 'react'
import Layout from '../layouts/Layout.jsx'
import { NavLink } from 'react-router-dom'
import '../styles/pages/Metrics.css'
import '@fortawesome/fontawesome-free/css/all.min.css';

const Metrics = () => {
    let id = 0;
    
    const getAllMetrics = async () => {
        try {
            const response = await fetch(`http://127.0.0.1:8000/api/v1/metrics`);
            const data = await response.json();
            return data; // Return the data array
        } catch (error) {
            console.error('Error fetching metrics:', error);
        }
    };
    
    const MetricRaws = () => {
        const [metricData, setMetricData] = useState(null);
        const [loading, setLoading] = useState(true);
    
        useEffect(() => {
            const fetchMetrics = async () => {
                const data = await getAllMetrics();
                setMetricData(data);
                setLoading(false); 
            };
    
            fetchMetrics(); 
        }, []);
    
        if (loading) {
            return <div>Loading...</div>; 
        }
    
        if (!metricData) {
            return <div>No data available</div>;
        }
    
        return metricData.map((metric, index) => (
            <tr key={index}>
                <th scope="row">{index + 1}</th>
                <td>{metric.name}</td>
                <td>{metric.description}</td>
                <td>{metric.type}</td>
                <td>{metric.area.join(',')}</td>
                <th>
                    <NavLink to={`/dashboard/metrics/view/${index + 1}`} 
                        className={(navData) => navData.isActive ? 'active' : ''}>
                        <button className="action-btn mx-1">
                            <i className="fa-solid fa-eye"></i>
                        </button>
                    </NavLink>
                    <NavLink to={`/dashboard/metrics/edit/${index + 1}`} 
                        className={(navData) => navData.isActive ? 'active' : ''}>
                        <button className="action-btn mx-1">
                            <i className="fa-solid fa-pen-to-square"></i>
                        </button>
                    </NavLink>
                </th>
            </tr>
        ))
            
    };
    

    return (
    <Layout>
        <div className="container my-5 px-5">
            <div className="row">
                <div className="col-md-12 d-flex justify-content-between">
                    <h1 className="mb-5" style={{ lineHeight: '.6' }}>Metrics List</h1>
                    <NavLink to="/dashboard/metrics/create" 
                    className={( (navData) => navData.isActive? 'active': '')}>
                        <button className="btn btn-primary" style={{ height: '40px', backgroundColor: '#6482AD' }}
                        type="button" value="Input">
                            Add New
                        </button>
                    </NavLink>
                </div>
                <table className="table table-striped">
                    <thead>
                        <tr>
                            <th scope="col">#</th>
                            <th scope="col">Name</th>
                            <th scope="col">Description</th>
                            <th scope="col">Type</th>
                            <th scope="col">Area</th>
                            <th scope="col">Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        <MetricRaws />
                    </tbody>
                </table>
            </div>
        </div>
    </Layout>
    )
}

export default Metrics