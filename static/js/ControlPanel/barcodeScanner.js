
$(document).scannerDetection({

	timeBeforeScanTest: 200,
	avgTimeByChar: 40,
	preventDefault: true,

	endChar: [13],

	onComplete: function (barcode, qty) {
		validScan = true;
	}
	,
	onError: function (string, qty) {
		let elem = document.getElementById(string);
		if (elem != null) {
			if (elem.classList.contains("isDoneStatus")) {
				registerNum([string], 3);
			} else {
				elem.classList.add("selected");
			}
		}
	}
});

