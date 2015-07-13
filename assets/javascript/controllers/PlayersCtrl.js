app.controller('PlayersCtrl', function($scope, players) {

    $scope.playerOptions = {
        data: players,
        paginationPageSizes: [10, 25, 50, 75, 100],
        paginationPageSize: 25,
        columnDefs: 
        [
            {
                field:'name', 
                displayName:'Name', 
                cellTemplate: '<div class="ngCellText"><a href="/player/{{ row.entity.id }}">{{ COL_FIELD }}</a></div>'
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
