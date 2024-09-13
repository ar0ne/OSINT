const axios = require('axios');

const API_URL = process.env.NEXT_PUBLIC_HOST_URL;

const isNumber = function isNumber(value) {
   return typeof value === 'number' && isFinite(value);
}


export const fetchScanPage = async (page) => {
  try {
    const pageNumber = isNumber(page) ? page : 1;
    const data = await axios.get(API_URL + "/scans/?page=" + pageNumber).then(
      response => response.data);
    return data; 
  } catch (error) {
    console.log(error);
  }
  return null;
};


export const fetchScanData = async (scan_id) => {
  try {
    const data = await axios.get(API_URL + "/scans/" + scan_id).
      then(response => response.data);
    return data; 
  } catch (error) {
    console.log(error);
  }
  return null;
};


export const fetchTools = async () => {
  try {
    return await axios.get(
      API_URL + "/tools"
    ).then(resp => resp.data.data);
  } catch (error) {
    console.log(error);
  }
  return [];
}
