function buttonClicked()
{
	$.ajax({
		url: "/unittestbutton",
		type: "get",
		datatype:"json",
		success: function(response){
			parsedResponse=JSON.parse(response);
			alert(parsedResponse.message);
			alert(parsedResponse.results);
		}
	});
};