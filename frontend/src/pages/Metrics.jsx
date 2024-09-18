import React, { useEffect, useState } from 'react'
import Layout from '../layouts/Layout.jsx'
import { NavLink } from 'react-router-dom'
import { getAllMetrics, handleDelete } from '../api/metrics/index.js'
import '../styles/pages/Metrics.css'
import '@fortawesome/fontawesome-free/css/all.min.css';

const MetricRaws = (props) => {
    useEffect(() => {
        const fetchMetrics = async () => {
            const data = await props.getAllMetrics();
            console.log("get data:: ", data);
            props.setMetricData(data);
            props.setLoading(false); 
        };

        fetchMetrics(); 
    }, []);

    if (props.loading) {
        return <div>Loading...</div>; 
    }

    if (!props.metricData) {
        return <div>No data available</div>;
    }

    return props.metricData.map((metric, index) => (
        <tr key={metric.id}>
            <th scope="row">{index + 1}</th>
            <td>{metric.name}</td>
            <td>{metric.description}</td>
            <td>{metric.type}</td>
            <td>{metric.area.join(',')}</td>
            <th>
                <NavLink to={`/dashboard/metrics/edit/${metric.id}`} 
                    className={(navData) => navData.isActive ? 'active' : ''}>
                    <button className="action-btn mx-1">
                        <i className="fa-solid fa-pen-to-square"></i>
                    </button>
                </NavLink>
                <button className="action-btn mx-1" 
                onClick={async () => {
                    const updatedMetrics = await props.handleDelete(metric.id);
                    props.setMetricData(updatedMetrics); // Set the updated metric data after delete
                }}>
                    <i className="fa-solid fa-trash"></i>
                </button>
            </th>
        </tr>
    ))
        
};


const Metrics = () => {
    const [metricData, setMetricData] = useState(null);
    const [loading, setLoading] = useState(true);
    
    return (
    <Layout>
        <div className="container my-5 px-5">
            <div className="row">
                <div className="col-md-12 d-flex justify-content-between">
                    <h1 className="mb-5">Metrics List</h1>
                    <NavLink to="/dashboard/metrics/create" 
                    className={( (navData) => navData.isActive? 'active': '')}>
                        <button className="btn btn-primary" id="add-new-btn"
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
                        <MetricRaws getAllMetrics={getAllMetrics} handleDelete={handleDelete}
                        metricData={metricData} setMetricData={setMetricData}
                        loading={loading} setLoading={setLoading}/>
                    </tbody>
                </table>
            </div>
        </div>
    </Layout>
    )
}

export default Metrics