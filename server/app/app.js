const express = require('express');
const app = express();
const port = 1337;
const cors = require('cors');
const dbModel = require('./db/index');

app.use(cors());
app.use(express.json());

app.get('/', async (req, res) => {
    const result = await dbModel.getData(dbModel.queries.getBike)

    res.json(result)
})

app.post('/update', async (req, res) => {
    const data = req.body;
    const date = new Date();
    const time = date.toLocaleString('se-SE', { timeZone: 'Europe/Stockholm' })
    const result = await dbModel.createData(dbModel.queries.createBike, [data.city_id, time])

    let response = {
        data: {
            msg: "all is good!"
        }
    }

    if (result.affectedRows == 0) {
        response.data = {
            errors: "all is NOT good"
        }
    }

    res.json(response)
})

app.listen(port, console.log(`App is listening on ${port}`));