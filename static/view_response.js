"use strict";

$("table").on("click", "button[id^=view_response]", getInfo);

function getInfo(evt) {
	evt.preventDefault();

	var job_id = evt.currentTarget.id.replace("view_response", "");

	var formInputs = {
		"job_id": job_id,
	};

	$.get("/job/response",
			formInputs,
			displayResponse);
}

function displayResponse(result) {
	if (result.response == "") {
		alert("Response for this job is not available.");
	}
	else {
		// var w = window.open();
		// w.document.write("<PLAINTEXT>")
		// w.document.write(result.response)
		var w = window.open();
		$(w.document.body).text(result.response);
		w.document.title = `Job ${result.job_id}`;
	}
}