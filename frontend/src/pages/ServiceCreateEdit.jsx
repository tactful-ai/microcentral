import React, { useState } from 'react'
import Layout from '../layouts/Layout'

const ServiceCreateEdit = (props) => {
  const [charLimit, setCharLimit] = useState(0);
  return (
    <Layout>
        <div className="content mt-4 mb-5 w-100">
            <div className="container">
                <div className="row">
                    <div className="col-sm-6 m-auto mb-5">
                        <h1 className="text-capitalize">{ props.mode } Service</h1>
                        <form mode={ props.mode } className="row g-3" id="service-form" onkeydown="return event.key != 'Enter';">
                            <div className="col-12">
                                <label for="service-name" className="form-label">Service Name</label>
                                <input type="text" className="form-control" placeholder="" id="service-name" />
                                <span className="error-msg text-danger d-none">error</span>
                            </div>
                            <div className="col-md-12">
                                <label for="service-description" className="form-label">Service Description </label>
                                <textarea className="form-control" placeholder="Write a brief descriptoin here" 
                                maxlength="{{char_limit}}" id="service-description" 
                                rows={4} onChange={(e)=>setCharLimit(e.target.value.length)}
                                ></textarea>
                                <div className="float-end"><span className="counter">{charLimit}</span>/100</div>
                                <span className="error-msg text-danger d-none">error</span>
                            </div>
                            <div className="col-12">
                                <label for="service-type" className="form-label">Service Scorecards</label>
                                <select className="form-select" name="" id="service-metrics">
                                    <option selected>Choose one of the scorecards</option>
                                    <option>scorecard 1</option>
                                    <option>scorecard 2</option>
                                </select>
                                <span className="error-msg text-danger d-none">error</span>
                            </div>
                            <div className="col-12">
                                <button type="submit" className="btn btn-primary col-12" id="create-btn" style={{backgroundColor: '#6482AD'}}>
                                    {props.mode == "create"? "Create": "Save"}
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </Layout>
  )
}

export default ServiceCreateEdit