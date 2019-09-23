
$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var numbers_received = [];

    //receive details from server
    socket.on('newnumber', function(msg) {
        console.log(JSON.stringify(msg));
        //maintain a list of ten numbers
        if (numbers_received.length >= 10){
            numbers_received.shift()
        }            
        numbers_received.push(msg.number);
        numbers_string = '';
        for (var i = 0; i < numbers_received.length; i++){
            numbers_string = numbers_string + '<div><p>' + numbers_received[i].toString() + '</p></div>';
        }
//          $('#log').html(numbers_string);
        $('#InProgContainer').html(numbers_string);
        $('#DoneContainer').html(numbers_string);
    });

});