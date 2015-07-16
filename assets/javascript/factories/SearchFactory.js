app.factory("searchFactory", function($http, $q, host) {
    var factory = {};

    factory.search = function(query) {
        return $http.get(host + "/resources/search?query=" + query);
    };

    return factory;
});
