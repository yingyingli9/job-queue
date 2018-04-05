"use strict";

$("#add_item_form").on("submit", getJobInfo);

function getJobInfo(evt) {
	evt.preventDefault();

	var formInputs = {
		"url": $("url").val()
	};

	$.post("/add_job",
			formInputs,
			processAdd);
}

function processAdd(result) {
	let html_content = `<tr>
							<td>
								${result.job_id}
							</td>
							<td>
								${result.url}
							</td>
						</tr>`;

	$("#new_job").prepend(html_content);


}