app.factory("playerFactory", function($http, $q, host) {
    var factory = {};

    factory.getPlayers = function() {
        return $http.get(host + "/resources/players", {cache: true});
    };

    factory.getPlayerDetail = function(id) {
        return $http.get(host +"/resources/player/" + id, {cache: true});
    };

    return factory;
});
