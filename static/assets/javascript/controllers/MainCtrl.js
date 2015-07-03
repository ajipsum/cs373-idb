app.controller('MainCtrl', ['$scope', function ($scope) {
 
  $scope.playerData = [
    {
        "firstName": "Cob",
        "company": "Enormo",
        "employed": true
    },
    {
        "firstName": "Lorraine",
        "company": "Comveyer",
        "employed": false
    },
    {
        "firstName": "Steve",
        "company": "Fuelton",
        "employed": false
    }
];

  $scope.teamData = [
    {
	"alpha": "1",
	"beta": "2"
    },
    {
	"alpha": "3",
	"beta": "4"
    }
];

  $scope.gameData = [
    {
	"gamma": "5",
	"delta": "6"
    },
    {
	"gamma": "7",
	"delta": "8"
    }
];

  $scope.playerOptions = {
      data: 'playerData',
      columnDefs: 
         [{
	      field:'firstName', 
	      displayName:'Alpha', 
	      cellTemplate: '<div class="ngCellText"><a href="/#/player/{[COL_FIELD]}">{[COL_FIELD]}</a></div>'
	  },
	  {
	      field: 'company', 
	      displayName:'Gamma'
	  },
	  {
	      field: 'employed', 
	      displayName:'Delta'
	  }]
  };

  $scope.teamOptions = {
      data: 'teamData',
      columnDefs: [{field:'alpha', displayName:'AlphaTest'},
		   {field:'beta', displayName:'BetaTest'}]
  };

  $scope.gameOptions = {
      data: 'gameData',
      columnDefs: [{field:'gamma', displayName:'GammaTest'},
		   {field:'delta', displayName:'DeltaTest'}]
  };


}]);
