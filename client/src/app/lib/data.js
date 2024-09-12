const axios = require('axios');


const isNumber = function isNumber(value) {
   return typeof value === 'number' && isFinite(value);
}


export const fetchScanPage = async (page) => {
  try {
    const pageNumber = isNumber(page) ? page : 1;
    const data = await axios.get("http://0.0.0.0:8000/api/v1/scans?page=" + pageNumber).
      then(response => response.data);
    return data; 
  } catch (error) {
    console.log(error);
  }
  return null;
};


export const fetchScanData = async (scan_id) => {
  try {
    const data = await axios.get("http://0.0.0.0:8000/api/v1/scans/" + scan_id).
      then(response => response.data);
    return data; 
  } catch (error) {
    console.log(error);
  }
  return null;
};
