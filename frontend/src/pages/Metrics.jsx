import React from 'react'
import Layout from '../layouts/Layout.jsx'
import { NavLink } from 'react-router-dom'
import '../styles/pages/Metrics.css'
import '@fortawesome/fontawesome-free/css/all.min.css';


const Metrics = () => {
    let id = 0;

    const getAllMetrics = async () => {
        var data = await fetch(`http://127.0.0.1:8000/api/v1/metrics`)
        .then((response) => response.json());
        
        var metric_data = data.object;
        console.log(metric_data);
    
    };
    
//   useEffect(()=> {
//     getAllMetrics()
//   }, [])

    const metrics = [
        {
            name: 'Metric 1',
            type: 'integer',
            tags: 'marketing, performance',
            description: 'Simple description for testing metric 1.'
        }
    ]

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
                        {metrics?.map((metric) => (
                            <tr key={id}>
                                <th scope="row">{++id}</th>
                                <td>{metric.name}</td>
                                <td>{metric.description}</td>
                                <td>{metric.type}</td>
                                <td>{metric.tags}</td>
                                <th>
                                    <NavLink to={`/dashboard/metrics/view/${id}`} 
                                    className={( (navData) => navData.isActive? 'active': '')}>
                                        <button className="action-btn mx-1">
                                            <i className="fa-solid fa-eye"></i>
                                        </button>
                                    </NavLink>
                                    <NavLink to={`/dashboard/metrics/edit/${id}`}  
                                    className={( (navData) => navData.isActive? 'active': '')}>
                                        <button className="action-btn mx-1">
                                            <i className="fa-solid fa-pen-to-square"></i>
                                        </button>
                                    </NavLink>
                                </th>
                            </tr>
                        ))}
                        <tr>
                            <th scope="row">{++id}</th>
                            <td>active-users</td>
                            <td>This metric counts the number of active users on the platform.</td>
                            <td>Integer</td>
                            <td>user engagement</td>
                            <th>--</th>
                        </tr>
                        <tr>
                            <th scope="row">{++id}</th>
                            <td>is-backup-completed</td>
                            <td>This metric indicates whether the backup process was completed successfully.</td>
                            <td>Boolean</td>
                            <td>data integrity</td>
                            <th>--</th>
                        </tr>
                        <tr>
                            <th scope="row">{++id}</th>
                            <td>failed-logins</td>
                            <td>This metric tracks the number of failed login attempts.</td>
                            <td>Integer</td>
                            <td>security</td>
                            <th>--</th>
                        </tr>
                        <tr>
                            <th scope="row">{++id}</th>
                            <td>is-service-running</td>
                            <td>This metric shows if a critical service is currently running.</td>
                            <td>Boolean</td>
                            <td>service status</td>
                            <th>--</th>
                        </tr>
                        <tr>
                            <th scope="row">{++id}</th>
                            <td>total-transactions</td>
                            <td>This metric counts the total number of transactions processed.</td>
                            <td>Integer</td>
                            <td>finance</td>
                            <th>--</th>
                        </tr>
                        <tr>
                            <th scope="row">{++id}</th>
                            <td>is-system-online</td>
                            <td>This metric indicates if the system is currently online.</td>
                            <td>Boolean</td>
                            <td>system status</td>
                            <th>--</th>
                        </tr>
                        <tr>
                            <th scope="row">{++id}</th>
                            <td>open-tickets</td>
                            <td>This metric counts the number of open support tickets.</td>
                            <td>Integer</td>
                            <td>customer support</td>
                            <th>--</th>
                        </tr>
                        <tr>
                            <th scope="row">{++id}</th>
                            <td>is-feature-enabled</td>
                            <td>This metric checks if a specific feature is enabled.</td>
                            <td>Boolean</td>
                            <td>feature management</td>
                            <th>--</th>
                        </tr>
                        <tr>
                            <th scope="row">{++id}</th>
                            <td>daily-registrations</td>
                            <td>This metric tracks the number of user registrations per day.</td>
                            <td>Integer</td>
                            <td>user acquisition</td>
                            <th>--</th>
                        </tr>
                        <tr>
                            <th scope="row">{++id}</th>
                            <td>is-payment-verified</td>
                            <td>This metric indicates whether a payment has been verified.</td>
                            <td>Boolean</td>
                            <td>payment processing</td>
                            <th>--</th>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </Layout>
    )
}

export default Metrics