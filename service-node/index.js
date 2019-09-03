const express = require('express')
const thrift = require('thrift');
const MicroService1 = require("./gen-nodejs/MicroService1")
const ttypes  = require("./gen-nodejs/demo_types")

var transport = thrift.TBufferedTransport;
var protocol = thrift.TBinaryProtocol;

/**
 * same server and protocol on which the other service is running
 */
var connection = thrift.createConnection("localhost", 6543, {
  transport : transport,
  protocol : protocol
});

connection.on('error', function(err) {
    console.log("false some error occured", err)
    process.exit(1)
});

var client = thrift.createClient(MicroService1, connection);

const app = express()
const port = 3000

app.get('/:id', (req, res) => {
    let userId = parseInt(req.params.id)
    client.getUser(userId, (err, user) => {
        if(err != null){
            res.statusCode = 404
            res.json(err)
        } else {
            res.json(user)
        }
    });
})

app.listen(port, () => console.log(`Example app listening on port ${port}!`))

