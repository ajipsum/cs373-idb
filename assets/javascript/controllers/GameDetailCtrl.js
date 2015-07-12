app.controller('GameDetailCtrl', ['$scope', function ($scope, game) {

	$scope.gameDate=game.date;
	$scope.awayId='awayTeamId_from_json'; //not implemented, need id from team (maybe foreign key)
	$scope.awayLogo='awayLogo_from_json'; //not implemented, team (or game) needs to store path to team logo
	$scope.homeId='homeTeamId_from_json'; //not implemented, need id from team (maybe foreign key)
	$scope.homeLogo='homeLogo_from_json'; //not implemented, team (or game) needs to store path to team logo
	$scope.awayName=game.away_team;
	$scope.awayScore=game.away_score;
	$scope.homeName=game.home_team;
	$scope.homeScore=game.home_score;
	$scope.awayPlayerObj=game.away_roster; //not implemented, need the roster from team
	$scope.homePlayerObj=game.home_roster; //not implemented, need the roster from team
	$scope.gameMapSource=game.google_maps;
	$scope.gameCitation=game.citation;

}]);
