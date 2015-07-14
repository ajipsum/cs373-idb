app.controller('PlayerDetailCtrl', ['$scope', 'player', '$sce', function ($scope, player, $sce) {

	$scope.playerHeadshot = player.picture;
	$scope.playerHeadshotBG = {'background': "linear-gradient(rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.2)), url('/assets/images/teambgs/" + player.team_name + ".png') #000 no-repeat center center"};
    $scope.playerName= player.name;
	$scope.playerNumber=player.player_number;
	$scope.playerPosition=player.position;
	$scope.teamId=player.team_name;
	$scope.teamName=player.current_team;
	$scope.twitterAccount=player.twitter;
    if (player.twitter != "N/A")
	    $scope.twitterDisplay="@" + player.twitter.replace("https://twitter.com/", "");
    else
        $scope.twitterDisplay = "";
	$scope.age=player.age;
	$scope.weight=player.weight;
	$scope.gameObj=player.schedule; //schedule is a list of game objects
	$scope.playerVideo=$sce.trustAsResourceUrl(player.youtube_link_1);
	$scope.playerMapSource=$sce.trustAsResourceUrl("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!" + player.google_maps);
	$scope.playerCitation=player.citation;
    
}]);
