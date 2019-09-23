
$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var numbers_received = [];

    //receive details from server
    socket.on('Result', function(msg) {
        console.log(JSON.stringify(msg));
        //maintain a list of ten numbers
        if (numbers_received.length >= 10){
            numbers_received.shift()
        }

        numbers_received.push(msg.objects);

        inPogress = '';
        Done = '';

        for (var i = 0; i < numbers_received.length; i++){

            if(numbers_received[i].toString() == "0"){
                inPogress  = inPogress + '<div><p>' + numbers_received[i].toString() + '</p></div>';
            }else{
                Done = Done + '<div><p>' + numbers_received[i].toString() + '</p></div>';
            }
        }
//          $('#log').html(numbers_string);
        $('#InProgContainer').html(inPogress);
        $('#DoneContainer').html(Done);
    });

});