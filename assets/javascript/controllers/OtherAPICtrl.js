app.controller('OtherAPICtrl', ['$scope', 'bplayer', 'fplayer', function ($scope, bplayer, fplayer) {
	
	$scope.weightButton = function()
	{

	}

	$scope.bPlayerPic=bplayer.picture;
	$scope.fPlayerPic=fplayer.photo;
	$scope.bPlayerName=bplayer.name;
	$scope.fPlayerName=fplayer.name;
	$scope.bPlayerWeight=bplayer.weight;
	$scope.fPlayerWeight=fplayer.wt;

}]);