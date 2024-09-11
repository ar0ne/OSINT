const axios = require('axios');

export const fetchScanData = async () => {
  try {
    const data = await axios.get("http://0.0.0.0:8000/api/v1/scans").
      then(response => response.data);
    return data; 
  } catch (error) {
    console.log(error);
  }
  return null;
};
