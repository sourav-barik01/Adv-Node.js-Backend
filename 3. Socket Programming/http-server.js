// This is HTTP, which is running on Application Layer & Can be accessed by Chrome
const http = require('http');

const server = http.createServer((req, res) => {
    console.log("New Connection Created");
    // res.end("Hi I am From Server Side - VS Code");
    if(req.url === '/home'){
        return res.end("Welcome Back To Home");
    } else {
        return res.end("Hi I am From Server Side - VS Code");
    }
});

server.listen(3000, () => {
    console.log("Server Started At Port : 3000");
});
