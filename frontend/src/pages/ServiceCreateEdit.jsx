import React, { useState, useEffect } from 'react'
import { useNavigate, useParams } from 'react-router-dom';
import Layout from '../layouts/Layout'
import { editService, getAllScorecrds, getAllTeams, getServiceById, postService } from '../api/services';

const ServiceCreateEdit = (props) => {
    const navigate = useNavigate();
  
    const {service_id} = useParams();
    const [tags, setTags] = useState([]);
    const [charLimit, setCharLimit] = useState(0);
    
    const [serviceName, setServiceName] = useState('');
    const [serviceDesc, setServiceDesc] = useState('');
    const [serviceTeam, setServiceTeam] = useState('');
    const [serviceScorecards, setServiceScorecards] = useState([]);

    const [teams, setTeams] = useState([]);
    const [scorecards, setScorecards] = useState([]);

    const handleFormSubmit = async (e) => {
        e.preventDefault();
        const service = {
            name: serviceName,
            description: serviceDesc,
            team_name: serviceTeam,
            scorecards: serviceScorecards
        }
        if (props.mode == "create"){
            await postService(service_id, service);
        }
        else if (props.mode == "edit"){
            await editService(service_id, service);
        }
        navigate('/dashboard/metrics', {state: { forceRender: true }});
    }

    const handleNameChange = (e) => {
        setServiceName(e.target.value);
    }
    const handleTeamChange = (e) => {
        setServiceTeam(e.target.value);
    }
    const handleDescChange = (e) => {
        setServiceDesc(e.target.value);
        setCharLimit(serviceDesc.length);
    }
    const handleScorecardsChange = (e) => {
        setServiceScorecards(e.target.value);
    }
    
    useEffect(() => {
        const fetchTeams = async() => {
            try{
                const teams_data = await getAllTeams();
                const teams_names = teams_data.map(team => team.name);
                setTeams(teams_names);

                // Getting all scorecards names for select menu
                // const scoreards_data = await getAllScorecrds();
                // const scorecards_names = scoreards_data.map(scorecard => scorecard.name);
                // setScorecards(scorecards_names);
            } catch (error) {
                console.log("error fetching service teams: ", error)
            }
        }
        fetchTeams();
        if (props.mode === 'edit') {
            const fetchService = async () => {
                try {
                    const service_data = await getServiceById(service_id, navigate);


                    setServiceName(service_data.name);
                    setServiceTeam(service_data.team_name);
                    setServiceDesc(service_data.description);
                } catch (error) {
                    console.error("Error fetching service data:", error);
                }
            };
            fetchService();
        }
    }, [service_id, props.mode]);
    
    
  return (
    <Layout>
        <div className="content mt-4 mb-5 w-100">
            <div className="container">
                <div className="row">
                    <div className="col-sm-6 m-auto mb-5">
                        <h1 className="text-capitalize">{ props.mode } Service</h1>
                        <form mode={ props.mode } className="row g-3" id="service-form"
                        onKeyDown={(e)=> {return e.key !== 'Enter'}}
                        onSubmit={(e) => handleFormSubmit(e)}>
                            <div className="col-12">
                                <label for="service-name" className="form-label">Service Name</label>
                                <input type="text" value={serviceName} onChange={(e) => handleNameChange(e)}
                                className="form-control" placeholder="" id="service-name" />
                                <span className="error-msg text-danger d-none">error</span>
                            </div>
                            <div className="col-12">
                                <label for="service-team" className="form-label">Service Team</label>
                                <select  value={serviceTeam} onChange={(e) => handleTeamChange(e)}
                                className="form-select" name="" id="service-team">
                                    {teams.map((team) => (
                                        <option key={team} value={team}>{team}</option>
                                    ))}
                                </select>
                                <span className="error-msg text-danger d-none">error</span>
                            </div>
                            <div className="col-md-12">
                                <label for="service-description" className="form-label">Service Description </label>
                                <textarea className="form-control" placeholder="Write a brief descriptoin here" 
                                maxlength="{{char_limit}}" id="service-description" 
                                rows={4} value={serviceDesc} onChange={(e) => handleDescChange(e)}
                                ></textarea>
                                <div className="float-end"><span className="counter">{charLimit}</span>/100</div>
                                <span className="error-msg text-danger d-none">error</span>
                            </div>
                            
                            {/* <div className="col-12">
                                <label for="service-scorecards" className="form-label">Service Scorecards</label>
                                <select  value={serviceScorecards} onChange={(e) => handleScorecardsChange(e)}
                                className="form-select" name="" id="service-scorecards">
                                    {scorecards.map((scorecard) => (
                                        <option key={scorecard} value={scorecard}>{scorecard}</option>
                                    ))}
                                </select>
                                <span className="error-msg text-danger d-none">error</span>
                            </div> */}
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
                                <button type="submit" className="btn btn-primary col-12"
                                id="create-btn" style={{backgroundColor: '#6482AD'}}>
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