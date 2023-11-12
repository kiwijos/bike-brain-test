const express = require('express');
const app = express();
const port = 1337;
const cors = require('cors');
const dbModel = require('./db/index');
const GeoJson = require('geojson');

const corsOptions = {
    origin: 'http://localhost:5000',
    credentials: true
};

app.use(cors(corsOptions));
app.use(express.json());

// Used for having multiple clients connect to /eventsource
let clients = [];

app.get('/', async (req, res) => {
    res.json({
        data: {
            msg: "Hello World! This is the root."
        }
    });
})

app.get('/eventsource', (req, res) => {
    res.setHeader('Content-Type', 'text/event-stream');
    res.setHeader('Cache-Control', 'no-cache');
    res.setHeader('Connection', 'keep-alive');


    // Add this client to the clients array
    clients.push(res);

    // Handle client disconnection
    req.on('close', () => {
        clients = clients.filter(client => client !== res);
    });
    
});

app.get('/get', async (req, res) => {
    const result = await dbModel.getData(dbModel.queries.getBike)

    res.json(result)
})

app.post('/update', async (req, res) => {
    const data = req.body;
    const jsonPoint = GeoJson.parse({
        lat: data.geometry[0],
        lng: data.geometry[1]
    },
    {
        Point: ['lat', 'lng']
    })
    const asString = JSON.stringify(jsonPoint);

    const result = await dbModel.updateData(dbModel.queries.updateBike, [asString, data.id])

    let response = {
        data: {
            msg: "all is good!"
        }
    }

    if (result.affectedRows == 0) {
        response.data = {
            errors: "all is NOT good"
        }
    } else {
        // Send data to all connected clients
        const eventData = {
            id: data.id,
            geoJSON: jsonPoint
        }
        // JSON.stringify(eventData)
        clients.forEach(client => {
            client.write(`data: ${JSON.stringify(eventData)}\n\n`);
        });
    }

    res.json(response)
})

app.listen(port, console.log(`App is listening on ${port}`));
