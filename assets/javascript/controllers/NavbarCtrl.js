app.controller('NavbarCtrl', function($scope){
    $scope.navTest = "LOAD NAVBAR HERE"

	$('.nav-collapse').click('li', function() {
		$('.nav-collapse').collapse('hide');
	});
});