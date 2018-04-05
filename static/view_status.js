"use strict";

$("table").on("click", "button[id^=view_status]", getInfo);

function getInfo(evt) {
	evt.preventDefault();

	var job_id = evt.currentTarget.id.replace("view_status", "");

	var formInputs = {
		"job_id": job_id,
	};

	$.post("/get_status",
			formInputs,
			displayStatus);
}

function displayStatus(result) {
	let html_content = `${result.job_status}`;

	$('#'+result.job_id).html(html_content);


}