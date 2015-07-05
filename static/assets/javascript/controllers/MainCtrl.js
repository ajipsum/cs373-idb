app.controller('MainCtrl', ['$scope', function ($scope) {
 
  $scope.playerData = [
    {
        "player_name": "Dwyane Wade",
        "current_team": "Miami Heat",
  "player_number": "3",
  "position": "SG",
  "age": "33",
  "weight": "220"
    },
    {
        "player_name": "Blake Griffin",
        "current_team": "Los Angeles Clippers",
  "player_number": "32",
  "position": "PF",
  "age": "26",
  "weight": "251"
    },
    {
        "player_name": "Tim Duncan",
        "current_team": "San Antonio Spurs",
  "player_number": "21",
  "position": "PF",
  "age": "39",
  "weight": "250"
    }
];

  $scope.teamData = [
    {
  "last_name": "Spurs",
  "city": "San Antonio",
  "state": "Texas",
  "site_name": "AT&T Center",
  "conference": "West",
  "division": "Southwest"
    },
    {
  "last_name": "Heat",
  "city": "Miami",
  "state": "Florida",
  "site_name": "AmericanAirlines Arena",
  "conference": "East",
  "division": "Southeast"
    },
    {
  "last_name": "Clippers",
  "city": "Los Angeles",
  "state": "California",
  "site_name": "Staples Center",
  "conference": "West",
  "division": "Pacific"
    }
];

  $scope.gameData = [
    {
  "game_id": "21400102",
  "home_team": "Los Angeles Clippers",
  "home_score": "89",
  "away_team": "San Antonio Spurs",
  "away_score": "85",
  "date": "November 10, 2014"
    },
    {
  "game_id": "21400414",
  "home_team": "San Antonio Spurs",
  "home_score": "125",
  "away_team": "Los Angeles Clippers",
  "away_score": "118",
  "date": "December 22, 2014"
    },
    {
  "game_id": "21400559",
  "home_team": "Los Angeles Clippers",
  "home_score": "104",
  "away_team": "Miami Heat",
  "away_score": "90",
  "date": "January 11, 2015"
    }
];

  $scope.playerOptions = {
      data: 'playerData',
      columnDefs: 
      [
    {
        field:'player_name', 
        displayName:'Name'//, 
        //cellTemplate: '<div class="ngCellText"><a href="/#/player/{[COL_FIELD]}">{[COL_FIELD]}</a></div>'
    },
    {
        field:'current_team', 
        displayName:'Team'
    },
    {
        field:'player_number', 
        displayName:'Number'
    },
    {
        field:'position',
        displayName:'Position'
    },
    {
        field:'age',
        displayName:'Age'
    },
    {
        field:'weight',
        displayName:'Weight'
    }
      ]
  };

  $scope.teamOptions = {
      data: 'teamData',
      columnDefs: 
      [
    {
        field:'last_name', 
        displayName:'Name'
    },
    {
        field:'city', 
        displayName:'City'
    },
    {
        field:'state',
        displayName:'State'
    },
    {
        field:'site_name',
        displayName:'Arena'
          },
    {
        field:'conference',
        displayName:'Conference'
    },
    {
        field:'division',
        displayName:'Division'
    }
      ]
  };

  $scope.gameOptions = {
      data: 'gameData',
      columnDefs: 
      [
    {
        field:'game_id', 
        displayName:'Game ID'
    },
    {
        field:'home_team', 
        displayName:'Home Team'
    },
    {
        field:'home_score',
        displayName:'Home Score'
    },
    {
        field:'away_team',
        displayName:'Away Team'
    },
    {
        field:'away_score',
        displayName:'Away Score'
    },
    {
        field:'date',
        displayName:'Date'
    }
      ]
  };


}]);