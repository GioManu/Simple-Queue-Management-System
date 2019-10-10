$(document).ready(function() {
  //connect to the socket server.
  var socket = io.connect(
    "http://" + document.domain + ":" + location.port + "/QueueMonitor"
  );
  var numbers_received = [];

  //receive details from server
  socket.on("Result", function(msg) {

    inPogress = "";
    Done = "";

    for (let [key, value] of Object.entries(msg.objects)) {
      if(value == "0"){
          closeChecksRequest([key],"1")
          console.log("SignalForNewOrder : " + key)
          inPogress =
          inPogress + '<div class="check_nums" ><p>' + key + "</p></div>";
      }
      else if (value == "1") {
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

async function closeChecksRequest(data, mode) {
  let url = `/registerNum/${mode}`;
  console.log(url);
  let response = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json;charset=utf-8"
    },
    body: JSON.stringify(data)
  });
}
