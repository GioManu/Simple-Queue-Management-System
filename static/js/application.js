$(document).ready(function() {
  //connect to the socket server.
  var socket = io.connect(
    "http://" + document.domain + ":" + location.port + "/QueueMonitor"
  );
  var numbers_received = [];

  //receive details from server
  socket.on("Result", function(msg) {
    //maintain a list of ten numbers
    if (numbers_received.length >= 10) {
      numbers_received.shift();
    }

    inPogress = "";
    Done = "";

    for (let [key, value] of Object.entries(msg.objects)) {
      if (value == "0") {
        inPogress =
          inPogress + '<div class="check_nums" ><p>' + key + "</p></div>";
      } else {
        Done = Done + '<div class="check_nums"><p>' + key + "</p></div>";
      }
    }

    $("#InProgContainer").html(inPogress);
    $("#DoneContainer").html(Done);
  });
});
