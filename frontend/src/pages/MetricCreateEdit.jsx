import React, { useState, useEffect, useRef } from 'react'
import { useParams, useNavigate } from 'react-router-dom';
import { Container, Row, Col, Button, Card, Carousel } from 'react-bootstrap';
import Layout from '../layouts/Layout';
import TagsBox from '../components/TagsBox';
import { getMetricById, editMetric, postMetric } from '../api/metrics';
import '../styles/pages/Metrics.css';


const MetricCreateEdit = (props) => {
  const navigate = useNavigate();

  const {metric_id} = useParams();
  const [tags, setTags] = useState([]);
  const [charLimit, setCharLimit] = useState(0);
  
  const [metricName, setMetricName] = useState('');
  const [metricType, setMetricType] = useState("integer");
  const [metricDesc, setMetricDesc] = useState('');

  const handleFormSubmit = async (e) => {
    e.preventDefault();
    if (props.mode == "create"){
        await postMetric(metricName, metricType, tags, metricDesc);
    }
    else if (props.mode == "edit"){
        await editMetric(metric_id, metricName, metricType, tags, metricDesc);
    }
    navigate('/dashboard/metrics', {state: { forceRender: true }});
  }

  const handleNameChange = (e) => {
    setMetricName(e.target.value);
  }
  const handleTypeChange = (e) => {
    setMetricType(e.target.value);
  }
  const handleDescChange = (e) => {
    setCharLimit(e.target.value.length);
    setMetricDesc(e.target.value);
  }

useEffect(() => {
    if (props.mode === 'edit') {
        const fetchMetricData = async () => {
            try {
                const metric_data = await getMetricById(metric_id, navigate);
                setMetricName(metric_data.name);
                setMetricType(metric_data.type);
                setMetricDesc(metric_data.description);
                setTags([...metric_data.area]);
            } catch (error) {
                console.error("Error fetching metric data:", error);
            }
        };
        fetchMetricData();
    }
}, [metric_id, props.mode]);


  return (
    <Layout>
        <div className="content mt-4 mb-5 w-100">
            <div className="container">
                <div className="row">
                    <div className="col-sm-6 m-auto mb-5">
                        <h1 className="text-capitalize">{props.mode} Metric</h1>
                        <form data-mode="create" className="row g-3" id="metric-form"
                        onKeyDown={(e)=> {return e.key !== 'Enter'}}
                        onSubmit={(e) => handleFormSubmit(e)}
                        >
                            <div className="col-12">
                                <label htmlFor="metric-name" className="form-label">Metric Name</label>
                                <input value={metricName} onChange={(e) => handleNameChange(e)}
                                type="text" className="form-control"placeholder="" 
                                id="metric-name" required></input>
                                <span className="error-msg text-danger d-none">error</span>
                            </div>
                            <div className="col-12">
                                <label htmlFor="metric-type" className="form-label">Metric Type</label>
                                <select value={metricType} onChange={(e) => handleTypeChange(e)}
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
                                <textarea value={metricDesc} onChange={(e) => handleDescChange(e)}
                                className="form-control" placeholder="Write a brief descriptoin here" maxLength="100" 
                                id="metric-description" rows={4}></textarea>
                                <div className="float-end"><span className="counter">{charLimit}</span>/100</div>
                                <span className="error-msg text-danger d-none">error</span>
                            </div>
                            <div className="col-12">
                                <button type="submit" className="btn btn-primary col-12" 
                                id="create-btn"
                                >
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