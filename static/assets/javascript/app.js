var app = angular.module('api2k15', [
    'ngTouch',
    'ui.grid'    
]);

app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[');
    $interpolateProvider.endSymbol(']}');
});
