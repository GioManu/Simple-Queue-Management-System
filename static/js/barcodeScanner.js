
$(document).scannerDetection({

	timeBeforeScanTest: 200,
	avgTimeByChar: 40,
	preventDefault: true,

	endChar: [13],

    onComplete: function(barcode, qty){
        validScan = true;
    }
	,
	onError: function(string, qty) {
        $('#userInput').val (string);
        closeChecksRequest([string],3);
        $('#userInput').val("");
	}
});

