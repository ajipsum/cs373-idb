app.controller('SearchCtrl', function($scope, $stateParams) {
    console.log($stateParams);
    $scope.results = $stateParams['results'];
    $scope.query = $stateParams['query'];
    console.log($scope.results);
});
