app.controller('AboutCtrl', ['$scope', 'bplayer', 'fplayer',function ($scope) {
	$scope.weightButton = function()
	{

	}

	$scope.bPlayerPic=bPlayer.picture;
	$scope.fPlayerPic=fplayer.photo;
	$scope.bPlayerName=bPlayer.name;
	$scope.fPlayerName=fPlayer.name;
	$scope.bPlayerWeight=bPlayer.weight;
	$scope.fPlayerWeight=fPlayer.wt;
}