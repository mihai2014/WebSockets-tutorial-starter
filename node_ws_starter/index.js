var http = require('http');
var static = require('node-static');
var fs = require('fs'); 

// static files in current directory
var file = new(static.Server)(__dirname);

// HTTP server
http.createServer(function (req, res) {
    file.serve(req, res);
}).listen(8000);
  
// WebSocket server

const WebSocket = require('ws');
const wss_sendEcho = new WebSocket.Server({ port: 8764 });
const wss_showTime = new WebSocket.Server({ port: 8765 });

console.log("started");


/*
  Events:
• open
• message
• error
• close
*/

/*
States:
WebSocket.CONNECTING    0 The connection is not yet open
WebSocket.OPEN          1 The connection is open and ready to communicate
WebSocket.CLOSING       2 The connection is in the process of closing
WebSocket.CLOSED        3 The connection is closed or couldn’t be opened
*/



wss_showTime.on('connection', function(ws) {
     
    setInterval(function sendTime(){
        var d = new Date();
        var time = `${d.getHours()} : ${d.getMinutes()} : ${d.getSeconds()}`
        console.log(`tick > ${time}`)
        ws.send(`${time}`);            
    }, 1000);

    ws.on('close', function() {
        console.log(`Conn closed (time socket)`)
    });  
    
});   


wss_sendEcho.on('connection', function(ws) {

    ws.on('message', function(received) {
        console.log(`received ${received}`)
        ws.send(`echo ${received}`);        
    })  

    ws.on('close', function() {
        console.log(`Conn closed (echo socket)`)
    });  
    
});   