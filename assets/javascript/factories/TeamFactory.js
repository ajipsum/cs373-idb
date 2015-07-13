app.factory("teamFactory", function($http, $q, host) {
    var factory = {};

    factory.getTeams = function() {
        return $http.get(host + "/resources/teams", {cache: true});
    };

    factory.getTeamDetail = function(id) {
        return $http.get(host +"/resources/team/view/" + id, {cache: true});
    };

    return factory;
});
