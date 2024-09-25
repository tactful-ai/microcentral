import React from 'react';
import '../../styles/layouts/Layout.css';

const NavBar = () => {
  return (
    <nav id="main-navbar">
      <div className="row">
          <div className="col-sm-6">
              <h5 className="mt-2" id="welcome-msg">
                Welcome, <span id="user-name">John</span>
              </h5>
          </div>
          <div className="col-sm-6">
              <div className="float-end" id="user-tools">
                <button className="user-icon align-middle px-1 mx-1">
                    <i className="fa fa-solid fa-bell"></i>
                </button>
                <button className="user-icon align-middle px-1 mx-1">
                    <i className="fa fa-solid fa-caret-down"></i>
                </button>
                <button className="align-middle px-1 mx-1" id="user-pic"></button>
              </div>
          </div>
      </div>
  </nav>
  )
}

export default NavBar