app.controller('PlayersCtrl', function($scope) {

    $scope.playerData = [
        {
            "player_name": "Dwyane Wade",
            "current_team": "Miami Heat",
            "player_number": "3",
            "position": "SG",
            "age": "33",
            "weight": "220",
            "tag": "dw"
        },
        {
            "player_name": "Blake Griffin",
            "current_team": "Los Angeles Clippers",
            "player_number": "32",
            "position": "PF",
            "age": "26",
            "weight": "251",
            "tag": "bg"
        },
        {
            "player_name": "Tim Duncan",
            "current_team": "San Antonio Spurs",
            "player_number": "21",
            "position": "PF",
            "age": "39",
            "weight": "250",
            "tag": "td"
        }
    ];

    $scope.playerOptions = {
        data: 'playerData',
        paginationPageSizes: [10, 25, 50, 75, 100],
        paginationPageSize: 25,
        columnDefs: 
        [
            {
                field:'player_name', 
                displayName:'Name', 
                cellTemplate: '<div class="ngCellText"><a href="/{{ row.entity.tag }}">{{ COL_FIELD }}</a></div>'
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
});
