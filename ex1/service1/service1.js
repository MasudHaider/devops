const express = require('express');
const axios = require('axios');
const fs = require('fs');

const app = express();
const logFile = '/usr/src/app/logs/service1.log';

fs.writeFileSync(logFile, '');

let counter = 1;
const interval = setInterval(async () => {
    try {
        const timestamp = new Date().toISOString();
        const logData = `${counter} ${timestamp}`;

        //fs.appendFileSync(logFile, logData + '\n');

        const response = await axios.post('http://service2_haider:8000/', logData, { // change to container name
            headers: {
                'Content-Type': 'text/plain'
            }
        });
        const addressPort = response.data.address;
        fs.appendFileSync(logFile, `${counter} ${timestamp} ${addressPort}\n`);
        counter++;

        if(counter > 20){
            clearInterval(interval);
            fs.appendFileSync(logFile, 'STOP\n');
            await axios.post('http://service2_haider:8000/', 'STOP', { //change to container name
                headers: {
                    'Content-Type': 'text/plain'
                }
            });
            process.exit(0);
        }
    } catch (error){
        fs.appendFileSync(logFile, `Error: ${error.message}\n`);
    }
}, 2000);

app.listen(8001, () => {
    console.log('service1 started on port 8001');
});