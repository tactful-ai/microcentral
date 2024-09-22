export const BASE_URL = "http://127.0.0.1:8000";
export const API_URL = "/api/v1";

export const getAllMetrics = async () => {
    try {
        const response = await fetch(`${BASE_URL}${API_URL}/metrics`);
        const data = await response.json();
        return data; // Return the data array
    } catch (error) {
        console.error('Error fetching metrics:', error);
    }
};

export const handleDelete = async (metric_id) => {
    try {
        const response = await fetch(`${BASE_URL}${API_URL}/metrics/${metric_id}`, {
            method: 'DELETE',
        });
        
        const data = await getAllMetrics();
        console.log(`Metric with id ${metric_id} deleted successfully`);
        return data;
    } catch (error) {
        console.error('Error deleting metric:', error);
    }
};

export const getMetricById = async (metric_id, navigate) => {
    try{
        var data = await fetch(`${BASE_URL}${API_URL}/metrics/${metric_id}`)
        .then((response) => response.json());
        
        if( data.message == "Not Found") {
            // replace path history to a 404 not found page
            navigate('/404');
        }
        var metric_data = data;
        console.log(metric_data);
        return metric_data;

    } catch (error) {
        console.log(error);
    }

};

export const editMetric = async (metric_id, metricName, metricType, tags, metricDesc) => {
    let formData = {
        name: metricName,
        type: metricType,
        area: tags,
        description: metricDesc
    }

    var data = await fetch(`${BASE_URL}${API_URL}/metrics/${metric_id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    })
    .then((response) => response.json())
    var responseData = {
        message: data.message,
        object: data
    }
    console.log(responseData)
}

export const postMetric = async (metricName, metricType, tags, metricDesc) => {
  let formData = {
      name: metricName,
      type: metricType,
      area: tags,
      description: metricDesc
  }

  var data = await fetch(`${BASE_URL}${API_URL}/metrics`, {
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
  console.log(responseData);
}