import React, { useState, useEffect } from 'react'
import { useNavigate, useParams } from 'react-router-dom';
import Layout from '../layouts/Layout'
import { editService, getAllScorecrds, getAllTeams, getServiceById, getServiceDetailsById, postService } from '../api/services';

const ServiceCreateEdit = (props) => {
    const navigate = useNavigate();
  
    const {service_id} = useParams();
    const [tags, setTags] = useState([]);
    const [charLimit, setCharLimit] = useState(0);
    
    const [serviceName, setServiceName] = useState('');
    const [serviceDesc, setServiceDesc] = useState('');
    const [serviceTeamName, setServiceTeamName] = useState('');
    const [serviceTeamId, setServiceTeamId] = useState('');

    const [serviceScorecards, setServiceScorecards] = useState([]);
    const [serviceScorecardId, setServiceScorecardId] = useState('');
    const [scorecardIds, setScorecardIds] = useState([]);

    const [teams, setTeams] = useState([]);
    const [scorecards, setScorecards] = useState([]);

    const handleFormSubmit = async (e) => {
        e.preventDefault();
        const service = {
            name: serviceName,
            description: serviceDesc,
            teamId: serviceTeamId,
            scorecardids: scorecardIds
        }
        console.log(service);
        if (props.mode == "create"){
            await postService(service_id, service);
        }
        else if (props.mode == "edit"){
            await editService(service_id, service);
        }
        navigate('/dashboard/services', {state: { forceRender: true }});
    }

    const handleNameChange = (e) => {
        setServiceName(e.target.value);
    }
    const handleTeamChange = (e) => {
        setServiceTeamId(e.target.value);
        setServiceTeamName(e.target.value);
        console.log(serviceTeamId)
    }
    const handleDescChange = (e) => {
        setServiceDesc(e.target.value);
        setCharLimit(e.target.value.length);
    }
    const handleScorecardsChange = (e) => {
        setServiceScorecardId(e.target.value);
        setServiceScorecards(e.target.value);
        console.log(serviceScorecardId)
    }
    
    useEffect(() => {
        const fetchFeildsData = async() => {
            try{
                // Getting all teams names for select menu
                const teams_data = await getAllTeams();
                setTeams(teams_data);

                // Getting all scorecards names for select menu
                const scorecards_data = await getAllScorecrds();
                setScorecards(scorecards_data);
            } catch (error) {
                console.log("error fetching service teams: ", error)
            }
        }
        fetchFeildsData();
        if (props.mode === 'edit') {
            const fetchService = async () => {
                try {
                    const service_data = await getServiceDetailsById(service_id, navigate);
                    setCharLimit(service_data.description.length)
                    setServiceName(service_data.name);
                    setServiceTeamName(service_data.team.name);
                    setServiceTeamId(service_data.teamId);
                    setServiceDesc(service_data.description);

                    service_data.scorecards.map((scorecard)=> {
                        setScorecardIds((prev) => [...prev, scorecard.id])
                    })
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
                                <select  value={serviceTeamName} onChange={(e) => handleTeamChange(e)}
                                className="form-select" name="" id="service-team">
                                    {teams.map((team) => (
                                        <option key={team.name} value={team.id}>{team.name}</option>
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
                            
                            <div className="col-12">
                                <label for="service-scorecards" className="form-label">Service Scorecards</label>
                                <select value={serviceScorecards} onChange={(e) => handleScorecardsChange(e)}
                                className="form-select" name="" id="service-scorecards">
                                    {scorecards.map((scorecard) => (
                                        <option key={scorecard.name} value={scorecard.id}>{scorecard.name}</option>
                                    ))}
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