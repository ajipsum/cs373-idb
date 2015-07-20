app.factory("otherFactory", function($http, $q, host) {
    var factory = {};

    factory.getBPlayer = function() {
    	id = Math.floor((Math.random() * 446) + 1);
        return $http.get(host + "/resources/player/view/" + id, {cache: true});
    };

    factory.getFPlayer = function() {
    	id = Math.floor((Math.random() * 14241) + 1);
    	return $http.get(host + "/resources/otherAPI/get_other_data" {cache: true});
    };

    return factory;
});