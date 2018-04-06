"use strict";

$("table").on("click", "button[id^=view_response]", getInfo);

function getInfo(evt) {
	evt.preventDefault();

	var job_id = evt.currentTarget.id.replace("view_response", "");

	var formInputs = {
		"job_id": job_id,
	};

	$.post("/get_response",
			formInputs,
			displayResponse);
}

function displayResponse(result) {
	if (result.response == "") {
		alert("Response for this job is not available.");
	}
	else {
		var w = window.open();
		w.document.write(`<TITLE>Job ${result.job_id}</TITLE>`);
		$(w.document).text(result.response);
	}
}