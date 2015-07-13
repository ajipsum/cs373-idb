app.controller('GameDetailCtrl', ['$scope', 'game', '$http', '$sce', function ($scope, game, $http, $sce) {

	$scope.gameDate=parseInt(game.date);
	$scope.awayId=game.away_team;
	$scope.awayLogo="/assets/images/teamlogos/" + game.away_team + ".png";
	$scope.homeId=game.home_team;
	$scope.homeLogo="/assets/images/teamlogos/" + game.home_team + ".png";
	$scope.awayName=game.away_team;
	$scope.awayScore=game.away_score;
	$scope.homeName=game.home_team;
	$scope.homeScore=game.home_score;
	$scope.awayPlayerObj=game.away_roster; //not implemented, need the roster from team
	$scope.homePlayerObj=game.home_roster; //not implemented, need the roster from team
	$http.get("/resources/team/" + game.home_team).success(function(response) {
		$scope.gameMapSource = $sce.trustAsResourceUrl("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!" + response.google_maps)
	});
	$scope.gameAwayCitation=game.citation.away;
	$scope.gameHomeCitation=game.citation.home;

}]);
