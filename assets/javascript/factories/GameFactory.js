app.factory("gameFactory", function($http, $q, host) {
    var factory = {};

    factory.getGames = function() {
        return $http.get(host + "/resources/games", {cache: true});
    };

    factory.getGameDetail = function(id) {
        return $http.get(host +"/resources/game/view/" + id, {cache: true});
    };

    return factory;
});
