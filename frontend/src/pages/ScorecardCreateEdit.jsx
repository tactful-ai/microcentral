import React, { useState, useEffect, useRef } from 'react'
import { useParams } from 'react-router-dom';
import TagsBox from '../components/TagsBox';
import axios from 'axios';
import Layout from '../layouts/Layout';
import '../styles/pages/Scorecards.css';

const ScorecardCreateEdit = (props) => {
    const {scorecard_id} = useParams();
    const [tags, setTags] = useState([]);
    const [charLimit, setCharLimit] = useState(0);
    
    const scorecardNameRef = useRef(null);
    const scorecardTypeRef = useRef(null);
    const scorecardDescRef = useRef(null);
      
  
    const postScorecard = (e) => {
      e.preventDefault();
      
      const scorecardName = scorecardNameRef.current;
      const scorecardType = scorecardTypeRef.current;
      const scorecardDesc = scorecardDescRef.current; 
  
      let formData = {
          name: scorecardName.value,
          type: scorecardType.value,
          area: tags,
          description: scorecardDesc.value
      }
  
      const response = async () => {
          var data = await fetch('http://127.0.0.1:8000/api/v1/scorecards', {
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
  
    const getScorecardById = async (scorecard_id) => {
      var data = await fetch(`http://127.0.0.1:8000/api/v1/scorecards/${scorecard_id}`)
      .then((response) => response.json());
      
      var scorecard_data = data.object;
      console.log(scorecard_data);
      
      const scorecardName = scorecardNameRef.current;
      const scorecardType = scorecardTypeRef.current;
      const scorecardDesc = scorecardDescRef.current; 
  
      scorecardName.value = scorecard_data.name;
      scorecardType.value = scorecard_data.type;
      scorecardDesc.value = scorecard_data.description;
  
      setTags([...scorecard_data.area]);
  
    };
  
    // useEffect(()=> {
    //   if(props.mode == 'edit'){
    //       getScorecardById(scorecard_id)
    //   }
    // }, [scorecard_id])
  
  
    return (
      <Layout>
        <div className="content mt-4 mb-5 w-100">
            <div className="container">
                <div className="row">
                    <div className="col-sm-6 m-auto mb-5">
                        <h1 className="text-capitalize">{ props.mode } Scorecard</h1>
                        <form mode={ props.mode } className="row g-3" id="scorecard-form" onkeydown="return event.key != 'Enter';">
                            <div className="col-12">
                                <label for="scorecard-name" className="form-label">Scorecard Name</label>
                                <input ref={scorecardNameRef} type="text" className="form-control" placeholder="" id="scorecard-name" />
                                <span className="error-msg text-danger d-none">error</span>
                            </div>
                            <div className="col-12">
                                <TagsBox label="Scorecard Services" tags={tags} setTags={setTags}/>
                                <span className="error-msg text-danger d-none">error</span>
                            </div>
                            <div className="col-md-12">
                                <label for="scorecard-description" className="form-label">Scorecard Description </label>
                                <textarea ref={scorecardDescRef} className="form-control" placeholder="Write a brief descriptoin here" 
                                maxlength="{{char_limit}}" id="scorecard-description" 
                                rows={4} onChange={(e)=>setCharLimit(e.target.value.length)}
                                ></textarea>
                                <div className="float-end"><span className="counter">{charLimit}</span>/100</div>
                                <span className="error-msg text-danger d-none">error</span>
                            </div>
                            <div className="col-12">
                                <label for="scorecard-type" className="form-label">Scorecard Metrics</label>
                                <select className="form-select" name="" id="scorecard-metrics">
                                    <option selected>Choose one of the metrics</option>
                                    <option>metric 1</option>
                                    <option>metric 2</option>
                                </select>
                                <ul id="metrics-list">
                                    <li className="metrics-item"></li>
                                </ul>
                                <span className="error-msg text-danger d-none">error</span>
                            </div>
                            <div className="col-12">
                                <button type="submit" className="btn btn-primary col-12" id="create-btn">
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

export default ScorecardCreateEdit