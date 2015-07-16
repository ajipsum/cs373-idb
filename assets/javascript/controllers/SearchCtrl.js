app.controller('SearchCtrl', function($scope, $stateParams) {
    $scope.results = $stateParams('results');
    $scope.query = $stateParams('query');
});
