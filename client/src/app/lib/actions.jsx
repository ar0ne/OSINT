'use server';


const axios = require("axios");


export async function createScan(formData) {
  
  const rawData = {
    tool: formData.get("tool");
    domain: formData.get("domain");
  };

  console.log(rawData);
}

