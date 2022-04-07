const { Board, Led } = require("johnny-five");
const board = new Board({
    port: "COM3"
});

board.on("ready",function(){
    let led = new Led(13);
    led.blink(500);
});