'use server';

import { z } from 'zod';
const axios = require("axios");

const FormSchema = z.object({
  tool: z.string(),
  domain: z.string().regex(/^[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,6}$/i),
});

const CreateInvoice = FormSchema.omit({});

const HOST_URL = process.env.HOST_URL;

export async function createScan (prevState, formData) {
  
  const validatedFields = CreateInvoice.safeParse({ 
    tool: formData.get("tool"),
    domain: formData.get("domain"),
  });

  if (!validatedFields.success) {
    return {
      errors: validatedFields.error.flatten().fieldErrors,
      message: 'Missing Fields. Failed to Create Scan.',
    };
  }

  const { tool, domain } = validatedFields.data;

  var result = await axios.post(HOST_URL + "/scans", 
    {tool_id: tool, domain: domain}
  ).then(resp => resp.data
  ).catch(err => err.response);

  if (result.status != 200) {
    return {
      message: result.data?.detail
    }
  }
}

