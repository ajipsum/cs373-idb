app.controller('TeamsCtrl', function($scope) {
    $scope.teamData = [
        {
            "last_name": "Spurs",
            "city": "San Antonio",
            "state": "Texas",
            "site_name": "AT&T Center",
            "conference": "West",
            "division": "Southwest",
            "mascot": "The Coyote",
            "tag": "sas"
        },
        {
            "last_name": "Heat",
            "city": "Miami",
            "state": "Florida",
            "site_name": "AmericanAirlines Arena",
            "conference": "East",
            "division": "Southeast",
            "mascot": "Burnie",
            "tag": "mia"
        },
        {
            "last_name": "Clippers",
            "city": "Los Angeles",
            "state": "California",
            "site_name": "Staples Center",
            "conference": "West",
            "division": "Pacific",
            "mascot": "Clippy",
            "tag": "lac"
        }
    ];

    $scope.teamOptions = {
        data: 'teamData',
        paginationPageSizes: [5, 10, 15, 30],
        paginationPageSize: 15,
        columnDefs: 
        [
            {
               field:'last_name', 
               displayName:'Name',
               cellTemplate: '<div class="ngCellText"><a href="/{{ row.entity.tag }}">{{ COL_FIELD }}</a></div>'
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
