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
	var w = window.open();
	$(w.document.body).html(result.response);


}