app.controller('SearchCtrl', function($scope, $stateParams) {
    $scope.results = $stateParams['results'];
    $scope.query = $stateParams['query'];
    $scope.noResults = true;
    

    if ($scope.results) {
        $scope.noResults = ($scope.results.teams == 0) && ($scope.results.games == 0) && ($scope.results.players == 0);
    } else {
        $scope.results = {
            "teams" : 0,
            "players" : 0,
            "games" : 0
        }
    }
});
