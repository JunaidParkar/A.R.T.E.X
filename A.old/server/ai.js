/*
 * Install the Generative AI SDK
 *
 * $ npm install @google/generative-ai
 *
 * See the getting started guide for more information
 * https://ai.google.dev/gemini-api/docs/get-started/node
 */

import { GoogleGenerativeAI, HarmCategory, HarmBlockThreshold } from "@google/generative-ai";
import { config } from "dotenv";

config()

const apiKey = process.env.ABC;


const GAN = async(prompt) => {
    let genAI = new GoogleGenerativeAI(apiKey);
    let model = genAI.getGenerativeModel({
        model: "gemini-1.5-flash",
    });
    let generationConfig = {
        temperature: 1,
        topP: 0.95,
        topK: 64,
        maxOutputTokens: 8192,
        responseMimeType: "text/plain",
    };
    let chatSession = model.startChat({
        generationConfig,
        history: [],
    });
    let result = await chatSession.sendMessage(prompt);
    return result.response.text();
}

const extractInformation = async(userInput) => {
    let genAI = new GoogleGenerativeAI(apiKey);
    let model = genAI.getGenerativeModel({
        model: "gemini-1.5-flash",
    });
    const prompt = `
    Extract the task, date, and time from the following input. If the date is not specified, write unspecified as string or if date is 'today or 'tomorrow' write it as it is and if the date and month is give then consider the year as 2024 and format as yyyy-mm-dd. If time is not specified write unspecified as string. If task is not specified write unspecified as string. Time should be in 24 hours format.
    
    Input: ${userInput}
    
    Output:
    Task: 
    Date: 
    Time: 
    `;
    let generationConfig = {
        temperature: 1,
        topP: 0.95,
        topK: 64,
        maxOutputTokens: 8192,
        responseMimeType: "application/json",
    };
    let session = model.startChat({ generationConfig, history: [] });
    const response = await session.sendMessage(prompt)
    const outputText = JSON.parse(response.response.text());
    const task = outputText["Task"];
    const date = outputText["Date"]
    const time = outputText["Time"]

    return { task, date, time };
}

export { GAN, extractInformation }