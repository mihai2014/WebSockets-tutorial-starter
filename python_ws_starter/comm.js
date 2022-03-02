window.addEventListener("DOMContentLoaded", () => {    
    const clock_div = document.querySelector('#clock');

    // get time
    const time_websocket = new WebSocket("ws://localhost:8765/");

    //old fashion def
    time_websocket.onmessage = function( event ) {
        clock_div.innerHTML = event.data;
    } 
    // arrow def   
    //time_websocket.onmessage = ( {data} ) => {
    //    clock_div.innerHTML = data;
    //};

    time_websocket.onclose = function(e) {
        clock_div.innerHTML = `Clock socket closed ${e.target.url}`;
    };
    //time_websocket.onclose = (e) => {
    //    clock_div.innerHTML = `Clock socket closed ${e.target.url}`;
    //};

    const messageResponse = document.querySelector('#response');

    //send echo message
    const echo_websocket = new WebSocket("ws://localhost:8764/");

    echo_websocket.onopen = function () {
        console.log('opened');
    };

    echo_websocket.onerror = function (error) {
        console.log('WebSocket Error ' + error);
    };

    echo_websocket.onmessage = function( event ) {
        messageResponse.innerHTML = event.data;
        console.log('received',event.data)
    } 

    document.querySelector('#send-message').onclick = function(e) {
        const messageInput = document.querySelector('#send');
        const message = messageInput.value;
        echo_websocket.send(message);
        messageInput.value = '';
    };

});