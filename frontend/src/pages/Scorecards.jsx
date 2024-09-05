import React from 'react'
import Layout from '../layouts/Layout'
import { NavLink } from 'react-router-dom'

const Scorecards = () => {
  return (
    <Layout>
        <div className="container my-5 px-5">
            <div className="row">
                <div className="col-md-12 d-flex justify-content-between">
                    <h1 className="mb-5" style={{ lineHeight: '.6' }}>Scorecards List</h1>
                    <NavLink to="/dashboard/scorecards/create" 
                    className={( (navData) => navData.isActive? 'active': '')}>
                        <button className="btn btn-primary" style={{ height: '40px', backgroundColor: '#6482AD' }}
                        type="button" value="Input">
                            Add New
                        </button>
                    </NavLink>
                </div>
            </div>
        </div>
    </Layout>
  )
}

export default Scorecards