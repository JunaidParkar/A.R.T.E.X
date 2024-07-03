// const { GoogleGenerativeAI } = require("@google/generative-ai");
// import { GoogleGenerativeAI } from '@google/generative-ai';
import { config as cfg } from 'dotenv';
cfg()

// Access your API key as an environment variable (see "Set up your API key" above)
// const genAI = new GoogleGenerativeAI(process.env.API_KEY);

// const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });
// console.log(genAI.getGenerativeModel())

import axios from 'axios';

async function getModels() {
    try {
        const response = await axios.get('https://api.makersuit.com/generative-ai/models', {
            // Add any necessary headers or authentication tokens
            headers: {
                'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
                'Content-Type': 'application/json'
            }
        });

        console.log('List of available models:');
        console.log(response.data);

    } catch (error) {
        console.error('Error fetching models:', error.response ? error.response.data : error.message);
    }
}

console.log(process.env.ABC)

getModels();