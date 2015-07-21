app.controller('OtherAPICtrl', ['$scope', 'bplayer', 'fplayer', function ($scope, bplayer, fplayer) {

	$scope.bPlayerPic=bplayer.picture;
	$scope.fPlayerPic=fplayer.photo;
	console.log(fplayer.photo);
	if (fplayer.photo == "") {
		$scope.fPlayerPic = "/assets/images/fplayer_default.png";
	};
	$scope.bPlayerName=bplayer.name;
	$scope.fPlayerName=fplayer.name;
	$scope.bPlayerWeight=bplayer.weight;
	$scope.fPlayerWeight=fplayer.wt;

}]);