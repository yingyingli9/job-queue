"use strict";

$("table").on("click", "button[id^=view_status]", getInfo);
$("#getJobStatus").on("submit", getID);

function getInfo(evt) {
	evt.preventDefault();

	var job_id = evt.currentTarget.id.replace("view_status", "");

	var formInputs = {
		"job_id": job_id,
	};

	$.get("/job/status",
			formInputs,
			displayStatus);
}

function displayStatus(result) {
	let job_status = `${result.job_status}`;

	$('#'+result.job_id).html(job_status);
	$('#view_status'+result.job_id).html('Refresh Status');
	if (result.job_status == "Not Completed" || result.job_status == "Invalid") {
		$('#view_response'+result.job_id).html("Response not Available");
	} else {
		$('#view_response'+result.job_id).html("View Response");
	}

}

function getID(evt) {

	evt.preventDefault();

	var job_id = $("#job_id").val();

	var formInputs = {
		"job_id": job_id,
	};

	$.get("/job/info",
			formInputs,
			popResponse);

}

function popResponse(result) {
	if (result.stop_process) {
		alert(result.message)
	} else {
		let statement = `Job ${result.job_id} is ${result.job_status}`;
		alert(statement);
		if (result.job_status == "Completed") {
			// var w = window.open('data:text/plain;charset=utf-8,' + result.response);
			var w = window.open();
			$(w.document.body).text(result.response);
			w.document.title = `Job ${result.job_id}`;
		}
	}
	$('#job_id').val('');
}

