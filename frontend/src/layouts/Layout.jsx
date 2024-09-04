import React from 'react'
import SideBar from '../components/layout/SideBar.jsx';
import NavBar from '../components/layout/NavBar.jsx';
import '../styles/layouts/Layout.css'

const Layout = ({ children }) => {
  return (
    <div className="layout">
      <div className="container-fluid">
        <div className="row vh-100">
          <div className="col-md-3">
            <SideBar />
          </div>
          <div className="col-md-9">
            <div className="col-md-12">
              <NavBar />
            </div>
            <div className="col-md-12">
              { children }
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Layout