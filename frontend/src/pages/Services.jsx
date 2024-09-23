import React, { useEffect, useState } from 'react'
import Layout from '../layouts/Layout.jsx'
import { NavLink } from 'react-router-dom'
// import { servicesData } from '../utils/data.js';
import { getAllServices, handleDelete } from '../api/services/index.js';

const ServicesRows = ({servicesData, setServicesData}) => {

    return servicesData.map((service, index) => (
        <tr key={index}>
            <th scope="row">{service.id}</th>
            <td>{service.name}</td>
            <td>{service.description}</td>
            <td>{service.team_name}</td>
            <td>{service.scorecard_names}</td>
            <th>
                <NavLink to={`/dashboard/services/${service.id}`}>
                    <button className="action-btn mx-1">
                        <i className="fa-solid fa-eye"></i>
                    </button>
                </NavLink>
                <NavLink to={`/dashboard/services/edit/${service.id}`}>
                    <button className="action-btn mx-1">
                        <i className="fa-solid fa-pen-to-square"></i>
                    </button>
                </NavLink>
                <button className="action-btn mx-1" onClick={async()=>{
                    handleDelete(service.id);
                    const updatedServices = await getAllServices();
                    setServicesData(updatedServices);
                }}>
                    <i className="fa-solid fa-trash"></i>
                </button>
            </th>
        </tr>
    ))
};

const Services = () => {
  const [servicesData, setServicesData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchServices = async () => {
        const data = await getAllServices();
        console.log("get data:: ", data);
        setServicesData(data);
        setLoading(false); 
    };

    fetchServices(); 
  }, []);

  
  return (
    <Layout>
        <div className="container my-5 px-5">
             <div className="row">
                 <div className="col-md-12 d-flex justify-content-between">
                     <h1 className="mb-5">Services List</h1>
                     <NavLink to="/dashboard/services/create" 
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
                            <th scope="col">Team</th>
                            <th scope="col">Scorecards</th>
                            <th scope="col">Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {loading ? (
                            <div>Loading...</div> 
                            ) : (
                            !servicesData ? (
                                <div>Data is loaded</div>
                            ) : (
                                <ServicesRows servicesData={servicesData}
                                setServicesData={setServicesData} />
                            )
                        )}
                    </tbody>
                </table>
            </div>
        </div>
    </Layout>
  )
}

export default Services