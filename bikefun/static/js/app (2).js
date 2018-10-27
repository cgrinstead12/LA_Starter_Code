var url = "/returndata";
// var mongoURL = "https://admin:USCbootcamp2018@ds141633.mlab.com:41633/la_events"
d3.json(mongoURL).then(function(eventData) {
	for (i = 0 ; i < eventData.length; i++) {
		console.log(eventData[1])
	}
	// console.log(eventData);

	// eventData.forEach(function(data) {
	// 	data.date = +data.date
});
// });