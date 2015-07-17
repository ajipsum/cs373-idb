app.controller('NavbarCtrl', function($scope, $state, searchFactory){
	$('.nav-collapse').click('li', function() {
		$('.nav-collapse').collapse('hide');
	});

    $scope.search = function() {
        if ($scope.searchString !== '') {
            searchFactory.search($scope.searchString).then(
                function(data) {
                    $state.go('root.search', {"results": data.data.results, "query": $scope.searchString});
                },
                function(error) {
                    console.log(error)
                }
            );
        }
    }
});
