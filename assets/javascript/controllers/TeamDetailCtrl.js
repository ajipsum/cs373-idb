app.controller('TeamDetailCtrl', ['$scope', 'team', '$sce', function ($scope, team, $sce) {

	$scope.teamLogo='/assets/images/teamlogos/' + team.name + '.png';
	$scope.teamName=team.name;
	$scope.conference=team.conference;
	$scope.division=team.division;
	$scope.playerObj=team.players;
	$scope.gameObj='gameObj_from_json'; //not implemented yet
	$scope.teamMapSource=$sce.trustAsResourceUrl("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!" + team.google_maps);
	$scope.teamCitation=team.citation;

}]);
