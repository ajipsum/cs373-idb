app.controller('GamesCtrl', function($scope, games) {

    $scope.gameOptions = {
        data: games,
        paginationPageSizes: [10, 25, 50, 75, 100],
        paginationPageSize: 25,
        columnDefs: 
        [
            {
                field:'id', 
                displayName:'Game ID',
                cellTemplate: '<div class="ngCellText"><a href="/game/{{ row.entity.id }}">{{ COL_FIELD }}</a></div>'
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
                displayName:'Date',
                cellFilter:'date:\'MM-dd-yyyy\''
            }
        ]
    };
});
