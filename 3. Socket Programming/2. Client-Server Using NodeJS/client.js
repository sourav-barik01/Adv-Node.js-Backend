const net = require('net');

// We are creating connection w/ the server using the same PORT
const client = net.createConnection({port:8080}, () => {
    console.log("Client Connected");
    client.write("Hello! From Node Client");
});

client.on('data', (serverData) => {         // on => When data recieved, then only it will go inside this function
    console.log("Data Recieved From Server is :", serverData.toString());
});
