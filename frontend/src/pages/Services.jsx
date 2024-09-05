import React, { useEffect, useState } from 'react'
import Layout from '../layouts/Layout.jsx'
import { NavLink } from 'react-router-dom'


const ServicesRaws = (props) => {
  useEffect(() => {
      const fetchService = async () => {
          const data = await props.getAllServices();
          console.log("get data:: ", data);
          props.setServiceData(data);
          props.setLoading(false); 
      };

      fetchService(); 
  }, []);

  if (props.loading) {
      return <div>Loading...</div>; 
  }

  if (!props.metricData) {
      return <div>No data available</div>;
  }

  return props.serviceData.map((service, index) => (
      <tr key={index}>
          <th scope="row">{index + 1}</th>
          <td>{service.name}</td>
          <td>{service.description}</td>
          <td>{service.type}</td>
          <td>{service.area.join(',')}</td>
          <th>
              <NavLink to={`/dashboard/services/edit/${service.id}`} 
                  className={(navData) => navData.isActive ? 'active' : ''}>
                  <button className="action-btn mx-1">
                      <i className="fa-solid fa-pen-to-square"></i>
                  </button>
              </NavLink>
              <button className="action-btn mx-1" onClick={()=>props.handleDelete(service.id)}>
                  <i className="fa-solid fa-trash"></i>
              </button>
          </th>
      </tr>
  ))
      
};


const Services = () => {
  const [serviceData, setServiceData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {console.log("re-rendered")}, []);
  const getAllServices = async () => {
      try {
          const response = await fetch(`http://127.0.0.1:8000/api/v1/services`);
          const data = await response.json();
          return data; // Return the data array
      } catch (error) {
          console.error('Error fetching service:', error);
      }
  };
  
  const handleDelete = async (service_id) => {
    try {
        const response = await fetch(`http://127.0.0.1:8000/api/v1/service/${service_id}`, {
            method: 'DELETE',
        });
        
        const data = await getAllServices();
        setServiceData(data);

        console.log(`Service with id ${service_id} deleted successfully`);
    } catch (error) {
        console.error('Error deleting service:', error);
    }
  };

  
  return (
    <Layout>
        <div className="container my-5 px-5">
            <div className="row">
                <div className="col-md-12 d-flex justify-content-between">
                    <h1 className="mb-5" style={{ lineHeight: '.6' }}>Services List</h1>
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
                        <ServicesRaws getAllServices={getAllServices} handleDelete={handleDelete}
                        serviceData={serviceData} setServiceData={setServiceData}
                        loading={loading} setLoading={setLoading}/>
                    </tbody>
                </table>
            </div>
        </div>
    </Layout>
    )
}

export default Services