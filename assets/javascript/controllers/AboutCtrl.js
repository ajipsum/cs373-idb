app.controller('AboutCtrl', function($scope) {
	$scope.buttonClicked = function()
	{
		$.ajax({
			url: "/unittestbutton",
			type: "get",
			datatype:"json",
			success: function(response){
				parsedResponse=JSON.parse(response);
				document.getElementById("errorbox").innerHTML = parsedResponse.results.split("\n").join("<br />");
			}
		});
	};
});
