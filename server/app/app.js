const express = require('express');
const app = express();
const port = 1337;
const cors = require('cors');

app.use(cors());

app.get('/', (req, res) => {
    res.send("Hej")
})

app.listen(port, console.log(`App is listening on ${port}`));