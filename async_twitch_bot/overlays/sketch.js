var socket = getSocketConnection()

setInterval(() => {
    if (socket.readyState === socket.CLOSED) {
        socket = getSocketConnection();
    }
}, 3000);

function getSocketConnection() {
    var socket = new WebSocket("ws://localhost:9999");

    socket.onerror = e => {
        console.log(`SOCKET ERROR: ${e}`);
    }
    socket.onclose = e => {
        console.log(`SOCKET CLOSED: ${e}`);
    }
    socket.onopen = e => {
        console.log(`SOCKET OPEN: ${e}`)
    }
    socket.onmessage = e => {
        let msg = e.data;
        console.log('ON MESSAGE');
        console.log('MSG ' + msg);
        if (msg == "test"){
            change = true;
            clearthing = true;
            holder = 1
            redraw()
        }
        if (msg == "test2"){
            change = true;
            clearthing = true;
            holder = 2
            redraw()
        }
        if (msg == "defeated"){
            boss = true;
            clearthing = true;
            redraw()
        }
        // if (msg == "clear"){
        //     change= false;
        // }

        
    }

    return socket;
}

var change = false;
var clearthing = false;
var boss = false;
var holder = null

function setup() {
    createCanvas(720, 400);
    img = loadImage("https://i1.wp.com/russgeorge.net/wp-content/uploads/2015/02/supermassive-black-hole_88846_990x742.jpg?resize=470%2C260");
    img2 = loadImage("https://images.beano.com/store/e4c5099fe0e1f85a9982b2e5af0db1997ac5e8168bea62585a40fe566944?auto=compress&w=752&h=423&format=jpg&frame=1");
    img3 = loadImage("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRMROMIylI8PgkMAbwM2W2lnYk_MXngOo9E_wSNaH6qWcstptXgaw");
    
}

function draw() {
    if (change & holder == 1) {       
        image(img, 0, 0);

    }else if (change & holder == 2){
        image(img2, 0, 0);

    }else if (boss){
        image(img3, 0, 0);

    }

    if (clearthing){
        setTimeout(clearscreen, 2000);
        clearthing = false;
    }

}

function clearscreen(){
    change = false;
    boss = false;
    clear()
}
