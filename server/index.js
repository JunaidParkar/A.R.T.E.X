import express from 'express';
import { GAN } from "./ai.js"
import bodyParser from 'body-parser';

// Create an instance of an Express application
const app = express();

app.use(bodyParser.json())

// Define a port to listen on
const port = process.env.PORT || 3000;

// Define a route handler for the default home page
app.post('/generateResponse', async(req, res) => {
    console.log(req.headers)
    let response = await GAN(req.body.prompt)
    res.json({ "response": response });
});

// Start the server and listen on the specified port
app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});