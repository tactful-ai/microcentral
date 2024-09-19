import React from 'react'
import { NavLink } from 'react-router-dom';

const SideBar = () => {
  return (
    <aside id="main-sidebar">
      <div className="container">
          <div className="row">
              <div className="">
                  <h3 id="logo">Microcentral</h3>
              </div>
              <div className="">
                  <ul id="sidebar-list">
                      <div className="row">
                        <li className="sidebar-item">
                            <NavLink to="/dashboard/services" 
                            className={( (navData) => navData.isActive? 'active': '')}>
                                Services
                            </NavLink>
                        </li>
                        <li className="sidebar-item">
                            <NavLink to="/dashboard/scorecards" 
                            className={( (navData) => navData.isActive? 'active': '')}>
                                Scorecards
                            </NavLink>
                        </li>
                        <li className="sidebar-item">
                            <NavLink to="/dashboard/metrics" 
                            className={( (navData) => navData.isActive? 'active': '')}>
                                Metrics
                            </NavLink>
                        </li>
                      </div>
                  </ul>
              </div>
          </div>
      </div>
  </aside>
  )
}

export default SideBar