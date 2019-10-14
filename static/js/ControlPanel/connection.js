$(document).ready(function () {
    //connect to the socket server.
    var socket = io.connect(
        "http://" + document.domain + ":" + location.port + "/QueueMonitor"
    );

    //receive details from server
    socket.on("Result", function (msg) {

        const MaxSize = 60;

        let orders = []

        let cont = document.getElementById("ordContainer");

        cont.innerHTML = "";

        for (let [key, value] of Object.entries(msg.objects)) {
            if (value == "0") {
                registerNum([key], "1")
                value = "1"
            }
            orders.push(prepareDiv(key, value))
        }

        orders.forEach((el) => {
            cont.append(el);
        });
    });
});

function prepareDiv(key, value) {
    let div = document.createElement("div");
    div.id = String(key);
    div.classList.add("ordNum");
    div.innerText = String(key);
    if (value == "2") {
        div.classList.add("isDoneStatus")
    } else {
        div.classList.add("inProgressStatus")
    }
    return div;
}

async function registerNum(data, mode) {
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
