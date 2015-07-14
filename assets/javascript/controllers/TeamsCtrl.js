app.controller('TeamsCtrl', function($scope, teams) {

    $scope.teamOptions = {
        data: teams,
        paginationPageSizes: [15, 30],
        paginationPageSize: 15,
        minRowsToShow: 16,
        columnDefs: 
        [
            {
               field:'name', 
               displayName:'Name',
               cellTemplate: '<div class="ngCellText"><a href="/teams/{{ row.entity.name }}">{{ COL_FIELD }}</a></div>'
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
            },
            {
                field:'mascot',
                displayName:'Mascot'
            }
        ]
    };
});
