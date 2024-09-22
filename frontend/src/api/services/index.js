const BASE_URL = 'http://127.0.0.1:8000'
const API_URL = 'api/v1'

export const handleDelete = async (service_id) => {
    try {
        const response = await fetch(`${BASE_URL}/${API_URL}/services/${service_id}`, {
            method: 'DELETE',
        });
        
        const data = await getAllServices();
        console.log(`Service with id ${service_id} deleted successfully`);

        return data;
    } catch (error) {
        console.error('Error deleting service:', error);
    }
};

export const postService = async (service_id, service) => {

    const request = {
        name: service.name,
        description: service.description,
        team_name: service.team_name,
        scorecards: service.scorecards
    }

    var data = await fetch(`${BASE_URL}/${API_URL}/services/${service_id}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(request),
    })
    .then((response) => response.json())
    var responseData = {
        message: data.message,
        object: data
    }
    console.log(responseData)
}

export const editService = async (service_id, service) => {

    const request = {
        name: service.name,
        description: service.description,
        teamId: service.teamId,
        scorecards: service.scorecards
    }

    var data = await fetch(`${BASE_URL}/${API_URL}/services/${service_id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(request),
    })
    .then((response) => response.json())
    var responseData = {
        message: data.message,
        object: data
    }
    console.log(responseData)
}

export const getAllServices = async () => {
    try {
        const response = await fetch(`${BASE_URL}/${API_URL}/services`);
        const data = await response.json();
        return data; // Return the data array
    } catch (error) {
        console.error('Error fetching services:', error);
    }
};

export const getAllTeams = async() => {
    try {
        const response = await fetch(`${BASE_URL}/${API_URL}/teams`);
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching teams:', error);
    }
}

export const getAllScorecrds = async() => {
    try {
        const response = await fetch(`${BASE_URL}/${API_URL}/scorecard/`);
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching scorecards:', error);
    }
}

export const getServiceById = async (service_id, navigate) => {
    try{
        
        const response = await fetch(`${BASE_URL}/${API_URL}/services/${service_id}`);
        const data = await response.json();
        
        if( data.message == "Not Found") {
            // replace path history to a 404 not found page
            navigate('/404');
        }

        console.log(data);
        return data; // Return the data array

    } catch (error) {
        console.log(error);
    }
};

export const getMetricReadings = async (service_id, from_date, to_date) => {
    let request = {
        service_id: service_id,
        from_date: from_date,
        to_date: to_date
    }

    var data = await fetch(`${BASE_URL}/${API_URL}/services/${service_id}/metric_readings`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(request),
    })
    .then((response) => response.json())
    var responseData = {
        message: data.message,
        object: data.object
    }
    console.log(responseData);
}

