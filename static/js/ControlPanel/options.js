let closeBtn = document.getElementById("CloseCheckButton");
let lis = document.getElementById("ordContainer");

lis.addEventListener("click", e => {
  e.preventDefault();
  if (e.target.classList.contains("ordNum")) {
    e.target.classList.toggle("selected");
  }
});

closeBtn.addEventListener("click", e => {
  let elems = document.getElementsByClassName("selected");
  data = [];

  for (let i = 0; i < elems.length; i++) {
    data.push(elems[i].innerText);
  }
  if (data.length > 0) {
    registerNum(data, 2);
  }
});
