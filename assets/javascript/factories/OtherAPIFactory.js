app.factory("otherFactory", function($http, host) {
    var factory = {};

    factory.getBPlayer = function(id) {
        return $http.get(host +"/resources/player/view/" + id, {cache: true});
    };

    factory.getFPlayer = function(id) {
    	return $http.get("cfdb.me:5000/punt/players/" + id, {cache: true});
    };

    return factory;
});