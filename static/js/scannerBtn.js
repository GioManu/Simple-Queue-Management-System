$(".animation_btn").on("click", e => {
  $(e.target).toggleClass("scan");
  if ($(".noise").length) {
    $(".noise").remove();
  } else {
    let noisy = document.createElement("div");
    $(noisy).addClass("noise");
    $(".parent").append(noisy);
    noise();
  }
});

function noise() {
  for (let i = 0; i < 00; i++) {
    let point = document.createElement("p");
    let span = document.createElement("span");
    let div = document.createElement("div");

    $(point).css({
      width: "1px",
      height: "1px",
      "background-color": "#006400",
      position: "absolute",
      top: Math.round(Math.random() * 200) - 30 + "%",
      left: Math.round(Math.random() * 200) + "%"
    });

    $(span).css({
      width: "1px",
      height: "1px",
      "background-color": "#00FF00",
      position: "absolute",
      top: Math.round(Math.random() * 200) - 30 + "%",
      left: Math.round(Math.random() * 200) + "%"
    });

    $(div).css({
      width: "1px",
      height: "1px",
      "background-color": "#00FA9A",
      position: "absolute",
      top: Math.round(Math.random() * 200) - 30 + "%",
      left: Math.round(Math.random() * 200) + "%"
    });

    $(".noise").append(point);
    $(".noise").append(span);
    $(".noise").append(div);
  }
}
