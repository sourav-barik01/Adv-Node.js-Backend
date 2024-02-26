const net = require('net');

// Making Socket Obj
const server = net.createServer((socket) => {
    socket.on('data', (clientData) => {     // on => When data recieved, then only it will go inside this function
        console.log("Data Recieved From Client is :", clientData);
        socket.write("Recieved On Server. Thank You!!");
    });
})

// Binding of HOST & PORT takes place in listen function only in Node.js
server.listen(8080, () => {
    console.log("New Server Up On PORT : 8080");
});
