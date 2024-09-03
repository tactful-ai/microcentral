import React, { useState, useEffect, useRef } from 'react'
import { useParams } from 'react-router-dom';
import TagsBox from '../components/TagsBox';
import axios from 'axios'
import Layout from '../layouts/Layout';


const MetricCreateEdit = (props) => {
    
  const {metric_id} = useParams();
  const [tags, setTags] = useState([]);
  const [charLimit, setCharLimit] = useState(0);
  
  const metricNameRef = useRef(null);
  const metricTypeRef = useRef(null);
  const metricDescRef = useRef(null);
    

  const postMetric = (e) => {
    e.preventDefault();
    
    const metricName = metricNameRef.current;
    const metricType = metricTypeRef.current;
    const metricDesc = metricDescRef.current; 

    let formData = {
        name: metricName.value,
        type: metricType.value,
        area: tags,
        description: metricDesc.value
    }

    const response = async () => {
        var data = await fetch('http://127.0.0.1:8000/api/v1/metrics', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        })
        .then((response) => response.json())
        var responseData = {
            message: data.message,
            object: data.object
        }
        console.log(responseData)
    };
    response();
  }

  const getMetricById = async (metric_id) => {
    var data = await fetch(`http://127.0.0.1:8000/api/v1/metrics/${metric_id}`)
    .then((response) => response.json());
    
    var metric_data = data.object;
    console.log(metric_data);
    
    const metricName = metricNameRef.current;
    const metricType = metricTypeRef.current;
    const metricDesc = metricDescRef.current; 

    metricName.value = metric_data.name;
    metricType.value = metric_data.type;
    metricDesc.value = metric_data.description;

    setTags([...metric_data.area]);

  };

  let disable = 'false'
  useEffect(()=> {
    if(props.mode == 'edit'){
        getMetricById(metric_id)
        if(props.mode == 'view'){
            disable = 'true'
        }
    }
  }, [metric_id])

  

  return (
    <Layout>
        <div className="content mt-4 mb-5" style={{width: '100%'}}>
            <div className="container">
                <div className="row">
                    <div className="col-sm-6 m-auto mb-5">
                        <h1 className="text-capitalize">{props.mode} Metric</h1>
                        <form data-mode="create" className="row g-3" id="metric-form"
                        onKeyDown={(e)=> {return e.key !== 'Enter'}}
                        onSubmit={(e) => e.preventDefault()}
                        >
                            <div className="col-12">
                                <label htmlFor="metric-name" className="form-label">Metric Name</label>
                                <input ref={metricNameRef} type="text" className="form-control"
                                placeholder="" id="metric-name"></input>
                                <span className="error-msg text-danger d-none">error</span>
                            </div>
                            <div className="col-12">
                                <label htmlFor="metric-type" className="form-label">Metric Type</label>
                                <select ref={metricTypeRef}
                                className="form-select" name="" id="metric-type">
                                    <option value="integer">integer</option>
                                    <option value="boolean">boolean</option>
                                </select>
                                <span className="error-msg text-danger d-none">error</span>
                            </div>
                            <div className="col-12">
                                <TagsBox label="Metric Area" tags={tags} setTags={setTags}/>
                                <span className="error-msg text-danger d-none">error</span>
                            </div>
                            <div className="col-md-12">
                                <label htmlFor="metric-description" className="form-label">Metric Description </label>
                                <textarea  ref={metricDescRef} className="form-control" 
                                placeholder="Write a brief descriptoin here" maxLength="100" 
                                id="metric-description" style={{height: '100px'}}
                                onChange={(e)=>setCharLimit(e.target.value.length)}></textarea>
                                <div className="float-end"><span className="counter">{charLimit}</span>/100</div>
                                <span className="error-msg text-danger d-none">error</span>
                            </div>
                            <div className="col-12">
                                <button type="submit" className="btn btn-primary col-12" 
                                id="create-btn" style={{backgroundColor: '#6482AD'}}
                                onClick={(e)=>postMetric(e)}>
                                    {props.mode == "create"? "Create": "Save"}
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </Layout>
  );
}

export default MetricCreateEdit;