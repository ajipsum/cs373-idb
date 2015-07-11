app.controller('PlayerDetailCtrl', ['$scope', 'player', function ($scope, player) {
    
    console.log(player);
	$scope.playerHeadshot = player.picture;
	$scope.playerName= player.name;
	$scope.playerNumber='playerNumber_from_json';
	$scope.playerPosition='playerPosition_from_json';
	$scope.teamId='teamId_from_json';
	$scope.teamName='teamName_from_json';
	$scope.twitterAccount='twitterAccount_from_json';
	$scope.age='age_from_json';
	$scope.weight='weight_from_json';
	$scope.gameObj='gameObj_from_json';
	$scope.playerVideo='playerVideo_from_json';
	$scope.playerMapSource='playerMapSource_from_json';
	$scope.playerCitation='playerCitation_from_json';

}]);
