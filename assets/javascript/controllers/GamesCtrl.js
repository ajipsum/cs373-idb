app.controller('GamesCtrl', function($scope, games) {

    $scope.gameData = [
        {
            "game_id": "21400102",
            "home_team": "Los Angeles Clippers",
            "home_score": "89",
            "away_team": "San Antonio Spurs",
            "away_score": "85",
            "date": "November 10, 2014",
            "tag": "g102"
        },
        {
            "game_id": "21400414",
            "home_team": "San Antonio Spurs",
            "home_score": "125",
            "away_team": "Los Angeles Clippers",
            "away_score": "118",
            "date": "December 22, 2014",
            "tag": "g414"
        },
        {
            "game_id": "21400559",
            "home_team": "Los Angeles Clippers",
            "home_score": "104",
            "away_team": "Miami Heat",
            "away_score": "90",
            "date": "January 11, 2015",
            "tag": "g559"
        }
    ];

    $scope.gameOptions = {
        data: 'gameData',
        paginationPageSizes: [10, 25, 50, 75, 100],
        paginationPageSize: 25,
        columnDefs: 
        [
            {
                field:'game_id', 
                displayName:'Game ID',
                cellTemplate: '<div class="ngCellText"><a href="/{{ row.entity.tag }}">{{ COL_FIELD }}</a></div>'
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
});
