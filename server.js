const https = require('https');
const http = require('http');
const express = require('express');
const app = express();
const fs = require('fs');
const path = require('path');
const port = process.env.PORT || 443;
const { spawn } = require('child_process');
const { PythonShell } = require('python-shell');

async function intervalFunc() {
  console.log("Hello!!!!");
  const pyProg = await spawn('python3', ['./jsonator.py']);
  pyProg.stdout.on('data', function (err, data) {
    if (err) {
      console.log('in error');
      console.log(err.toString());
    }
    console.log("response of deployed token", data);
    // res.write(data);
    console.log('end python')
  })
}
setInterval(intervalFunc, 300000);


app.use(express.static(__dirname + '/'));


app.get('/*', function (req, res) {
  res.sendFile(path.join(__dirname + '/index.html'));
});


// Start the app by listening on the default
app.listen(8080);
console.log('Server has started ... @ PORT : ' + 80);


