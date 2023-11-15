const express = require('express');
const router = express.Router();
const dbModel = require('../db/index');
const GeoJson = require('geojson');

// Used for having multiple clients connect to /eventsource
let clients = [];

router.get('/', async (req, res) => {
    res.json({
        data: {
            msg: "Hello World! This is the root."
        }
    });
})

router.get('/eventsource', (req, res) => {
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

router.get('/get', async (req, res) => {
    const result = await dbModel.getData(dbModel.queries.getBike)

    res.json(result)
})

router.post('/update', async (req, res) => {
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

module.exports = router;
