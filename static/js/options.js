let closeBtn = document.getElementById("CloseCheckButton");
let lis = document.getElementById("InProgContainer");

lis.addEventListener("click", e => {
  if (e.target.parentElement.classList.contains("check_nums")) {
    e.target.parentElement.classList.toggle("selected");
  }
});

closeBtn.addEventListener("click", e => {
  let elems = document.getElementsByClassName("selected");
  data = [];

  for (let i = 0; i < elems.length; i++) {
    data.push(elems[i].firstChild.innerText);
  }
  if (data.length > 0) {
    closeChecksRequest(data, 2);
  }
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