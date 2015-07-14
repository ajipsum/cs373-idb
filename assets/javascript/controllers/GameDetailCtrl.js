app.controller('GameDetailCtrl', ['$scope', 'game', '$http', '$sce', function ($scope, game, $http, $sce) {

	$scope.gameDate=parseInt(game.date*1000);
	$scope.awayId=game.away_team;
	$scope.awayLogo="/assets/images/teamlogos/" + game.away_team + ".png";
	$scope.homeId=game.home_team;
	$scope.homeLogo="/assets/images/teamlogos/" + game.home_team + ".png";
	$scope.awayName=game.away_team;
	$scope.awayScore=game.away_score;
	$scope.homeName=game.home_team;
	$scope.homeScore=game.home_score;
	$scope.awayRoster=game.roster.away;
	$scope.homeRoster=game.roster.home;
	$scope.gameMapSource=$sce.trustAsResourceUrl("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!" + game.google_maps);
	$scope.gameAwayCitation=game.citation.away;
	$scope.gameHomeCitation=game.citation.home;

}]);
