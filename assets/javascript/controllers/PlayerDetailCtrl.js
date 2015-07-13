app.controller('PlayerDetailCtrl', ['$scope', 'player', '$http', '$sce', function ($scope, player, $http, $sce) {

	$scope.playerHeadshot = player.picture;
	$scope.playerName= player.name;
	$scope.playerNumber=player.playerNumber;
	$scope.playerPosition=player.position;
	$scope.teamId=player.team_name;
	$scope.teamName=player.current_team;
	$scope.twitterAccount=player.twitter;
	$scope.age=player.age;
	$scope.weight=player.weight;
	$scope.gameObj=player.schedule; //schedule is a list of game objects
	$scope.playerVideo=$sce.trustAsResourceUrl(player.youtube_link_1);
	$http.get("/resources/team/" + player.team_name).success(function(response) {
		$scope.playerMapSource = $sce.trustAsResourceUrl("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!" + response.google_maps)
	});
	$scope.playerCitation=player.citation;

}]);
