$(document).ready(function () {
    //connect to the socket server.
    var socket = io.connect(
        "http://" + document.domain + ":" + location.port + "/QueueMonitor"
    );

    //receive details from server
    socket.on("Result", function (msg) {

        const MaxSize = 12;

        inPogress = [];
        Done = [];

        for (let [key, value] of Object.entries(msg.objects)) {
            if (value == "0") {
                registerNum([key], "1")
                inPogress.push(key);
            }
            else if (value == "1") {
                inPogress.push(key);
            } else {
                Done.push(key);
            }
        }

        pushToScreen(inPogress, MaxSize, "InProgContainer");
        pushToScreen(Done, MaxSize, "DoneContainer", true);

    });
});

function pushToScreen(arr, MaxSize, containerID, isDone = false) {
    let cont = document.getElementById(containerID);
    cont.innerHTML = "";

    let tmp = arr.slice(0, MaxSize);

    tmp.forEach((e) => {
        let div = document.createElement("div");
        div.id = `num${e}`;
        div.classList.add("ordNum");
        div.innerText = String(e);
        cont.append(div);
        if (isDone) {
            div.classList.add("blink")
        }
    })
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
