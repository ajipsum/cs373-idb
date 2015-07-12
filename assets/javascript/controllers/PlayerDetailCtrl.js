app.controller('PlayerDetailCtrl', ['$scope', 'player', function ($scope, player) {
    
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
	$scope.playerVideo=player.youtube_link_1;
	$scope.playerMapSource='playerMapSource_from_json';
	$scope.playerCitation=player.citation;

}]);
